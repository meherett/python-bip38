#!/usr/bin/env python3

# Copyright © 2023, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Tuple, Union, Optional, List, Dict, Literal
)
from pyaes import AESModeOfOperationECB

import scrypt
import unicodedata
import os

from .utils import (
    integer_to_bytes, bytes_to_integer, bytes_to_string, get_bytes, double_sha256, hash160
)
from .libs.base58 import (
    encode, check_encode, decode, check_decode, ensure_string
)

# Wallet important format prefix
WIF_PREFIX: int = 0x80
# Bitcoin Pay to Public Key Hash (P2PKH) address prefixes
ADDRESS_PREFIXES: Dict[Literal["mainnet", "testnet"], int] = {
    "mainnet": 0x00, "testnet": 0x6f
}
# BIP38 non-EC-multiplied & EC-multiplied private key prefixes
BIP38_NO_EC_MULTIPLIED_PRIVATE_KEY_PREFIX: int = 0x0142
BIP38_EC_MULTIPLIED_PRIVATE_KEY_PREFIX: int = 0x0143
# Wallet important format flags
BIP38_NO_EC_MULTIPLIED_WIF_FLAG: int = 0xc0
BIP38_NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG: int = 0xe0
# Magic bytes for lot and sequence and non lot and sequence
MAGIC_LOT_AND_SEQUENCE: int = 0x2ce9b3e1ff39e251
MAGIC_NO_LOT_AND_SEQUENCE: int = 0x2ce9b3e1ff39e253
# Magic uncompressed and compressed flags
MAGIC_LOT_AND_SEQUENCE_UNCOMPRESSED_FLAG: int = 0x04
MAGIC_LOT_AND_SEQUENCE_COMPRESSED_FLAG: int = 0x24
MAGIC_NO_LOT_AND_SEQUENCE_UNCOMPRESSED_FLAG: int = 0x00
MAGIC_NO_LOT_AND_SEQUENCE_COMPRESSED_FLAG: int = 0x20
# Confirmation code prefix
CONFIRMATION_CODE_PREFIX: int = 0x643bf6a89a
# The proven prime
P: int = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1
# Number of points in the field
N: int = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
# These two defines the elliptic curve. y^2 = x^3 + A-curve * x + B-curve
A_CURVE, B_CURVE = 0, 7
# This is our generator point. Trillions of dif ones possible
G_POINT: Tuple[int, int] = (
    55066263022277343669578718895168534326250603453777594175500187360389116729240,
    32670510020758816978083085130507043184471273380659243275938904335757337482424
)
# Private key prefixes
UNCOMPRESSED_PRIVATE_KEY_PREFIX: int = 0x00
COMPRESSED_PRIVATE_KEY_PREFIX: int = 0x01
# Public key prefixes
EVEN_COMPRESSED_PUBLIC_KEY_PREFIX: int = 0x02
ODD_COMPRESSED_PUBLIC_KEY_PREFIX: int = 0x03
UNCOMPRESSED_PUBLIC_KEY_PREFIX: int = 0x04
# Checksum byte length
CHECKSUM_BYTE_LENGTH: int = 4
# List of compression, lot_and_sequence, non_ec, ec, & illegal flags
FLAGS: Dict[str, List[int]] = {
    "compression": [
        MAGIC_NO_LOT_AND_SEQUENCE_COMPRESSED_FLAG, MAGIC_LOT_AND_SEQUENCE_COMPRESSED_FLAG,
        0x28, 0x2c, 0x30, 0x34, 0x38, 0x3c, 0xe0, 0xe8, 0xf0, 0xf8
    ],
    "lot_and_sequence": [
        MAGIC_LOT_AND_SEQUENCE_UNCOMPRESSED_FLAG, MAGIC_LOT_AND_SEQUENCE_COMPRESSED_FLAG,
        0x0c, 0x14, 0x1c, 0x2c, 0x34, 0x3c
    ],
    "non_ec": [
        BIP38_NO_EC_MULTIPLIED_WIF_FLAG, BIP38_NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG,
        0xc8, 0xd0, 0xd8, 0xe8, 0xf0, 0xf8
    ],
    "ec": [
        0x00, 0x04, 0x08, 0x0c, 0x10, 0x14, 0x18, 0x1c, 0x20, 0x24, 0x28, 0x2c, 0x30, 0x34, 0x38, 0x3c
    ],
    "illegal": [
        0xc4, 0xcc, 0xd4, 0xdc, 0xe4, 0xec, 0xf4, 0xfc
    ]
}


# Greatest common divisor: Extended Euclidean Algorithm/'division' in elliptic curves
def mod_inv(a: int, n: int = P) -> int:
    lm, hm = 1, 0
    resto = a % n
    high = n
    while resto > 1:
        ratio = high // resto
        nm = hm - lm * ratio
        new = high - resto * ratio
        lm, resto, hm, high = nm, new, lm, resto
    return lm % n


# Not true addition, invented for EC. Could have been called anything
def ec_add(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    LamAdd = ((b[1] - a[1]) * mod_inv(b[0] - a[0], P)) % P
    x = (LamAdd * LamAdd - a[0] - b[0]) % P
    y = (LamAdd * (a[0] - x) - a[1]) % P
    return x, y


# This is called point doubling, also invented for EC
def ec_double(a: Tuple[int, int]) -> Tuple[int, int]:
    Lam = ((3 * a[0] * a[0] + A_CURVE) * mod_inv((2 * a[1]), P)) % P
    x = (Lam * Lam - 2 * a[0]) % P
    y = (Lam * (a[0] - x) - a[1]) % P
    return x, y


# Double & add. Not true multiplication
def ecc_multiply(gen_point: tuple, scalar_hex: int) -> Tuple[int, int]:
    if scalar_hex == 0 or scalar_hex >= N:
        raise ValueError("Invalid scalar/private key")
    # Binary string without beginning 0b
    scalar_bin = str(bin(scalar_hex))[2:]
    # This is a tuple of two integers of the point of generation of the curve
    q: Tuple[int, int] = gen_point
    for index in range(1, len(scalar_bin)):
        q = ec_double(q)
        if scalar_bin[index] == "1":
            q = ec_add(q, gen_point)
    return q


# Iterative Function to calculate (x^y) % z in O(log y)
def pow_mod(x: int, y: int, z: int) -> int:
    n = 1
    while y:
        if y & 1:
            n = n * x % z
        y >>= 1
        x = x * x % z
    return n


def get_checksum(raw: bytes) -> bytes:
    return double_sha256(raw)[:CHECKSUM_BYTE_LENGTH]


def uncompress_public_key(public_key: Union[str, bytes]) -> str:
    """
    Uncompress public key converter

    :param public_key: Public key
    :type public_key: Union[str, bytes]

    :returns: str -- Uncompressed public key

    >>> from bip38 import uncompress_public_key
    >>> uncompress_public_key(public_key="0348ca8b4e7c0c75ecfd4b437535d186a12f3027be0c29d2125e9c0dec48677caa")
    '0448ca8b4e7c0c75ecfd4b437535d186a12f3027be0c29d2125e9c0dec48677caacb4cd50b4c5ea3313a69402c8b0a336b183d39ea18215ff69f59fdb540f00559'
    """

    public_key: bytes = get_bytes(public_key)
    yp = bytes_to_integer(public_key[:1]) - 2
    x = bytes_to_integer(public_key[1:])
    a = (pow_mod(x, 3, P) + 7) % P
    y = pow_mod(a, (P + 1) // 4, P)
    if y % 2 != yp:
        y = -y % P
    return bytes_to_string(
        integer_to_bytes(UNCOMPRESSED_PUBLIC_KEY_PREFIX) + integer_to_bytes(x) + integer_to_bytes(y)
    )


def compress_public_key(public_key: Union[str, bytes]) -> str:
    """
    Compress public key converter

    :param public_key: Public key
    :type public_key: Union[str, bytes]

    :returns: str -- Compressed public key

    >>> from bip38 import compress_public_key
    >>> compress_public_key(public_key="0448ca8b4e7c0c75ecfd4b437535d186a12f3027be0c29d2125e9c0dec48677caacb4cd50b4c5ea3313a69402c8b0a336b183d39ea18215ff69f59fdb540f00559")
    '0348ca8b4e7c0c75ecfd4b437535d186a12f3027be0c29d2125e9c0dec48677caa'
    """

    public_key: bytes = get_bytes(public_key)
    x, y = public_key[1:33], public_key[33:]
    if bytes_to_integer(y) % 2:
        return bytes_to_string(
            integer_to_bytes(ODD_COMPRESSED_PUBLIC_KEY_PREFIX) + x
        )
    else:
        return bytes_to_string(
            integer_to_bytes(EVEN_COMPRESSED_PUBLIC_KEY_PREFIX) + x
        )


def multiply_private_key(private_key_1: bytes, private_key_2: bytes) -> bytes:
    return integer_to_bytes(
        (
            bytes_to_integer(private_key_1) * bytes_to_integer(private_key_2)
        ) % N
    )


def multiply_public_key(public_key: bytes, private_key: bytes, public_key_type: Literal["uncompressed", "compressed"] = "compressed") -> bytes:

    if len(public_key) == 33:
        public_key = get_bytes(uncompress_public_key(public_key))

    x, y = ecc_multiply(
        (
            bytes_to_integer(public_key[1:33]), bytes_to_integer(public_key[33:])
        ),
        bytes_to_integer(private_key)
    )
    if public_key_type == "uncompressed":
        return get_bytes(bytes_to_string(
            integer_to_bytes(UNCOMPRESSED_PUBLIC_KEY_PREFIX) + integer_to_bytes(x) + integer_to_bytes(y)
        ))
    elif public_key_type == "compressed":
        return get_bytes(compress_public_key(bytes_to_string(
            integer_to_bytes(UNCOMPRESSED_PUBLIC_KEY_PREFIX) + integer_to_bytes(x) + integer_to_bytes(y)
        )))
    else:
        raise ValueError(f"Invalid public key type (expected uncompressed/compressed, got {public_key_type!r})")


def private_key_to_public_key(private_key: Union[str, bytes], public_key_type: Literal["uncompressed", "compressed"] = "compressed") -> str:
    """
    Private key to public key converter

    :param private_key: Private key
    :type private_key: Union[str, bytes]
    :param public_key_type: Public key type, default to ``compressed``
    :type public_key_type: Literal["uncompressed", "compressed"]

    :returns: str -- Public key

    >>> from bip38 import private_key_to_public_key
    >>> private_key_to_public_key(private_key="cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5")
    '02d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360e'
    >>> private_key_to_public_key(private_key="cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5", public_key_type="uncompressed")
    '04d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360ea7f23327b49ba7f10d17fad15f068b8807dbbc9e4ace5d4a0b40264eefaf31a4'
    """

    # Get the public key point
    x, y = ecc_multiply(
        G_POINT, bytes_to_integer(get_bytes(private_key))
    )

    if public_key_type == "uncompressed":
        public_uncompressed: bytes = (
                integer_to_bytes(UNCOMPRESSED_PUBLIC_KEY_PREFIX) + integer_to_bytes(x) + integer_to_bytes(y)
        )
        return public_uncompressed.hex()
    elif public_key_type == "compressed":
        public_compressed: bytes = (
            (   # If the Y value for the Public Key is odd
                integer_to_bytes(ODD_COMPRESSED_PUBLIC_KEY_PREFIX) + integer_to_bytes(x)
            ) if y & 1 else (
                integer_to_bytes(EVEN_COMPRESSED_PUBLIC_KEY_PREFIX) + integer_to_bytes(x)
            )   # Or else, if the Y value is even
        )
        return public_compressed.hex()
    else:
        raise ValueError(f"Invalid public key type (expected uncompressed/compressed, got {public_key_type!r})")


def encode_wif(private_key: Union[str, bytes]) -> Tuple[str, str]:
    if len(get_bytes(private_key)) != 32:
        raise ValueError(f"Invalid private key length (expected 64, got {len(private_key)!r})")

    wif_payload: bytes = (
        integer_to_bytes(WIF_PREFIX) + get_bytes(private_key)
    )
    wif_compressed_payload: bytes = (
        integer_to_bytes(WIF_PREFIX) + get_bytes(private_key) + integer_to_bytes(COMPRESSED_PRIVATE_KEY_PREFIX)
    )
    return (
        encode(wif_payload + get_checksum(wif_payload)), encode(wif_compressed_payload + get_checksum(wif_compressed_payload))
    )


def private_key_to_wif(private_key: Union[str, bytes], wif_type: Literal["wif", "wif-compressed"] = "wif-compressed") -> str:
    """
    Private key to Wallet Important Format (WIF) converter

    :param private_key: Private key
    :type private_key: Union[str, bytes]
    :param wif_type: Wallet Important Format (WIF) type, default to ``wif-compressed``
    :type wif_type: Literal["wif", "wif-compressed"]

    :returns: str -- Wallet Important Format

    >>> from bip38 import private_key_to_wif
    >>> private_key_to_wif(private_key="cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5")
    'L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP'
    >>> private_key_to_wif(private_key="cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5", wif_type="wif")
    '5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR'
    """

    # Getting uncompressed and compressed
    wif, wif_compressed = encode_wif(private_key=private_key)

    if wif_type == "wif":
        return wif
    elif wif_type == "wif-compressed":
        return wif_compressed
    else:
        raise ValueError("Invalid WIF type, choose only 'wif' or 'wif-compressed' types")


def decode_wif(wif: str) -> Tuple[bytes, Literal["wif", "wif-compressed"], bytes]:
    raw: bytes = decode(wif)
    if not raw.startswith(integer_to_bytes(0x80)):
        raise ValueError(f"Invalid wallet important format")

    prefix_length: int = len(integer_to_bytes(WIF_PREFIX))
    prefix_got: bytes = raw[:prefix_length]
    if integer_to_bytes(WIF_PREFIX) != prefix_got:
        raise ValueError(f"Invalid WIF prefix (expected {prefix_length!r}, got {prefix_got!r})")

    raw_without_prefix: bytes = raw[prefix_length:]

    checksum: bytes = raw_without_prefix[-1 * 4:]
    private_key: bytes = raw_without_prefix[:-1 * 4]
    wif_type: Literal["wif", "wif-compressed"] = "wif"

    if len(private_key) not in [33, 32]:
        raise ValueError(f"Invalid wallet important format")
    elif len(private_key) == 33:
        private_key = private_key[:-len(integer_to_bytes(COMPRESSED_PRIVATE_KEY_PREFIX))]
        wif_type = "wif-compressed"

    return private_key, wif_type, checksum


def wif_to_private_key(wif: str) -> str:
    """
    Wallet Important Format (WIF) to Private key converter

    :param wif: Wallet Important Format
    :type wif: str

    :returns: str -- Private key

    >>> from bip38 import wif_to_private_key
    >>> wif_to_private_key(wif="L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP")
    'cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5'
    >>> wif_to_private_key(wif="5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR")
    'cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5'
    """

    return bytes_to_string(decode_wif(wif=wif)[0])


def get_wif_type(wif: str) -> Literal["wif", "wif-compressed"]:
    """
    Get Wallet Important Format (WIF) type

    :param wif: Wallet Important Format
    :type wif: str

    :returns: Literal["wif", "wif-compressed"] -- WIF type

    >>> from bip38 import get_wif_type
    >>> get_wif_type(wif="L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP")
    'wif-compressed'
    >>> get_wif_type(wif="5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR")
    'wif'
    """

    return decode_wif(wif=wif)[1]


def get_wif_checksum(wif: str) -> str:
    """
    Get Wallet Important Format (WIF) checksum

    :param wif: Wallet Important Format
    :type wif: str

    :returns: str -- WIF checksum

    >>> from bip38 import get_wif_checksum
    >>> get_wif_checksum(wif="L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP")
    'dc37f844'
    >>> get_wif_checksum(wif="5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR")
    'f0a25c0c'
    """

    return bytes_to_string(decode_wif(wif=wif)[2])


def public_key_to_addresses(public_key: Union[str, bytes], network: Literal["mainnet", "testnet"] = "mainnet") -> str:
    """
    Public key to address converter

    :param public_key: Public key
    :type public_key: Union[str, bytes]
    :param network: Network type
    :type network: Literal["mainnet", "testnet"], default to ``mainnet``

    :returns: str -- Address

    >>> from bip38 import public_key_to_addresses
    >>> public_key_to_addresses(public_key="02d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360e", network="mainnet")
    '164MQi977u9GUteHr4EPH27VkkdxmfCvGW'
    >>> public_key_to_addresses(public_key="04d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360ea7f23327b49ba7f10d17fad15f068b8807dbbc9e4ace5d4a0b40264eefaf31a4", network="mainnet")
    '1Jq6MksXQVWzrznvZzxkV6oY57oWXD9TXB'
    >>> public_key_to_addresses(public_key="02d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360e", network="testnet")
    'mkaJhmE5vvaXG17uZdCm6wKpckEfnG4yt9'
    >>> public_key_to_addresses(public_key="04d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360ea7f23327b49ba7f10d17fad15f068b8807dbbc9e4ace5d4a0b40264eefaf31a4", network="testnet")
    'myM3eoxWDWxFe7GYHZw8K21rw7QDNZeDYM'
    """
    
    if network not in ["mainnet", "testnet"]:
        raise ValueError(f"Invalid Bitcoin network, (expected: 'mainnet' or 'testnet', got: {network})")

    # Getting public key hash
    public_key_hash: bytes = hash160(get_bytes(public_key))
    payload: bytes = (
        integer_to_bytes(ADDRESS_PREFIXES[network]) + public_key_hash
    )
    return ensure_string(encode(payload + get_checksum(payload)))


def intermediate_code(
    passphrase: str, lot: Optional[int] = None, sequence: Optional[int] = None, owner_salt: Union[str, bytes] = os.urandom(8)
) -> str:
    """
    Intermediate passphrase generator

    :param passphrase: Passphrase or password text
    :type passphrase: str
    :param lot: Lot number  between 100000 <= lot <= 999999 range, default to ``None``
    :type lot: Optional[int]
    :param sequence: Sequence number  between 0 <= sequence <= 4095 range, default to ``None``
    :type sequence: Optional[int]
    :param owner_salt: Owner salt, default to ``os.urandom(8)``
    :type owner_salt: Optional[str, bytes]

    :returns: str -- Intermediate passphrase

    >>> from bip38 import intermediate_code
    >>> intermediate_code(passphrase="TestingOneTwoThree")
    'passphraseqVKbgU4mWMakKGgCtaeVWoETQdzMBy5696bG2w7ckVBeQmoLhMF9vLaxhmzhT3'
    >>> intermediate_code(passphrase="TestingOneTwoThree", lot=199999, sequence=1, owner_salt="75ed1cdeb254cb38")
    'passphraseb7ruSN4At4Rb8hPTNcAVezfsjonvUs4Qo3xSp1fBFsFPvVGSbpP2WTJMhw3mVZ'
    """

    owner_salt: bytes = get_bytes(owner_salt)
    if len(owner_salt) not in [4, 8]:
        raise ValueError(f"Invalid owner salt length (expected 8/16, got {len(bytes_to_string(owner_salt))!r})")
    if len(owner_salt) == 4 and (not lot or not sequence):
        raise ValueError(f"Invalid owner salt length for non lot/sequence (expected 16, got {len(bytes_to_string(owner_salt))!r})")
    if (lot and not sequence) or (not lot and sequence):
        raise ValueError(f"Both lot & sequence are required, got (lot {lot!r}) (sequence {sequence!r})")

    if lot and sequence:
        lot, sequence = int(lot), int(sequence)
        if not 100000 <= lot <= 999999:
            raise ValueError(f"Invalid lot, (expected 100000 <= lot <= 999999, got {lot!r})")
        if not 0 <= sequence <= 4095:
            raise ValueError(f"Invalid lot, (expected 0 <= sequence <= 4095, got {sequence!r})")

        pre_factor: bytes = scrypt.hash(unicodedata.normalize("NFC", passphrase), owner_salt[:4], 16384, 8, 8, 32)
        owner_entropy: bytes = owner_salt[:4] + integer_to_bytes((lot * 4096 + sequence), 4)
        pass_factor: bytes = double_sha256(pre_factor + owner_entropy)
        magic: bytes = integer_to_bytes(MAGIC_LOT_AND_SEQUENCE)
    else:
        pass_factor: bytes = scrypt.hash(unicodedata.normalize("NFC", passphrase), owner_salt, 16384, 8, 8, 32)
        magic: bytes = integer_to_bytes(MAGIC_NO_LOT_AND_SEQUENCE)
        owner_entropy: bytes = owner_salt

    pass_point: str = private_key_to_public_key(
        private_key=bytes_to_string(pass_factor), public_key_type="compressed"
    )
    return ensure_string(check_encode(
        magic + owner_entropy + get_bytes(pass_point)
    ))


def bip38_encrypt(wif: str, passphrase: str, network: Literal["mainnet", "testnet"] = "mainnet") -> str:
    """
    BIP38 Encrypt wallet important format using passphrase/password

    :param wif: Wallet important format
    :type wif: str
    :param passphrase: Passphrase or password text
    :type passphrase: str
    :param network: Network type
    :type network: Literal["mainnet", "testnet"], default to ``mainnet``

    :returns: str -- Encrypted wallet important format

    >>> from bip38 import bip38_encrypt
    >>> bip38_encrypt(wif="5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR", passphrase="TestingOneTwoThree")
    '6PRVWUbkzzsbcVac2qwfssoUJAN1Xhrg6bNk8J7Nzm5H7kxEbn2Nh2ZoGg'
    >>> bip38_encrypt(wif="L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP", passphrase="TestingOneTwoThree")
    '6PYNKZ1EAgYgmQfmNVamxyXVWHzK5s6DGhwP4J5o44cvXdoY7sRzhtpUeo'
    """

    wif_type: Literal["wif", "wif-compressed"] = get_wif_type(wif=wif)
    if wif_type == "wif":
        flag: bytes = integer_to_bytes(BIP38_NO_EC_MULTIPLIED_WIF_FLAG)
        private_key: str = wif_to_private_key(wif=wif)
        public_key_type: Literal["uncompressed", "compressed"] = "uncompressed"
    elif wif_type == "wif-compressed":
        flag: bytes = integer_to_bytes(BIP38_NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG)
        private_key: str = wif_to_private_key(wif=wif)
        public_key_type: Literal["uncompressed", "compressed"] = "compressed"
    else:
        raise ValueError("Wrong wallet important format type")

    public_key: str = private_key_to_public_key(
        private_key=private_key, public_key_type=public_key_type
    )
    address: str = public_key_to_addresses(public_key=public_key, network=network)
    address_hash: bytes = get_checksum(get_bytes(address, unhexlify=False))
    key: bytes = scrypt.hash(unicodedata.normalize("NFC", passphrase), address_hash, 16384, 8, 8)
    derived_half_1, derived_half_2 = key[0:32], key[32:64]

    aes: AESModeOfOperationECB = AESModeOfOperationECB(derived_half_2)
    encrypted_half_1: bytes = aes.encrypt(integer_to_bytes(
        bytes_to_integer(get_bytes(private_key[0:32])) ^ bytes_to_integer(derived_half_1[0:16])
    ))
    encrypted_half_2: bytes = aes.encrypt(integer_to_bytes(
        bytes_to_integer(get_bytes(private_key[32:64])) ^ bytes_to_integer(derived_half_1[16:32])
    ))

    encrypted_private_key: bytes = (
        integer_to_bytes(BIP38_NO_EC_MULTIPLIED_PRIVATE_KEY_PREFIX) + flag + address_hash + encrypted_half_1 + encrypted_half_2
    )
    return ensure_string(encode(
        encrypted_private_key + get_checksum(encrypted_private_key)
    ))


def create_new_encrypted_wif(
    intermediate_passphrase: str,
    public_key_type: Literal["uncompressed", "compressed"] = "uncompressed",
    seed: Union[str, bytes] = os.urandom(24),
    network: Literal["mainnet", "testnet"] = "mainnet"
) -> dict:
    """
    Create new encrypted wallet important format

    :param intermediate_passphrase: Intermediate passphrase text
    :type intermediate_passphrase: str
    :param public_key_type: Public key type, default to ``uncompressed``
    :type public_key_type: Literal["uncompressed", "compressed"]
    :param seed: Seed, default to ``os.urandom(24)``
    :type seed: Optional[str, bytes]
    :param network: Network type
    :type network: Literal["mainnet", "testnet"], default to ``mainnet``

    :returns: dict -- Encrypted wallet important format

    >>> from bip38 import create_new_encrypted_wif
    >>> create_new_encrypted_wif(intermediate_passphrase="passphraseb7ruSN4At4Rb8hPTNcAVezfsjonvUs4Qo3xSp1fBFsFPvVGSbpP2WTJMhw3mVZ")
    {'encrypted_wif': '6PgGSHicUccU2dotWbwJd514DqWdmCM4KFNYiP4poXgC57qfUpEkKbTj9U', 'confirmation_code': 'cfrm38V8Foq3WpRPMXJD34SF6pGT6ht5ihYMWWMbezkzHgPpA1jVkfbTHwQzvuSA4ReF86PHZJY', 'public_key': '045cd5348750657daa7ef756582cbd5564fe6f65a4a4370fcc234f642826c8e43ec927612179c2768cf616fd1a2f1ccfbf91a5529daf2d8439f366fc9c8ae7dc71', 'seed': 'b6b1122e418c4e188de3f57588119f0f5bdc780f52c3f677', 'public_key_type': 'uncompressed', 'address': '1JbyXoVN4hXWirGB265q9VE4pQ6qbY6kmr'}
    >>> create_new_encrypted_wif(intermediate_passphrase="passphraseb7ruSN4At4Rb8hPTNcAVezfsjonvUs4Qo3xSp1fBFsFPvVGSbpP2WTJMhw3mVZ", public_key_type="compressed", seed="99241d58245c883896f80843d2846672d7312e6195ca1a6c")
    {'encrypted_wif': '6PoM8coZNg4AGPhQs91RbmmRmfLz6kmnU3XUGGLQxsJ5xN62LsUzMWYcdP', 'confirmation_code': 'cfrm38VXL5T6qVke13sHUWtEjibAkK1RquBqMXb2azCv1Zna6JKvBhD1Gf2b15wBj7UPv2BQnf6', 'public_key': '02100bb0440ff4106a1743750813271e66a7017431e92921e520319f537c7357c1', 'seed': '99241d58245c883896f80843d2846672d7312e6195ca1a6c', 'public_key_type': 'compressed', 'address': '15PuNwFmDqYhRsC9MDPNFvNY4Npzibm67c'}
    """

    seed_b: bytes = get_bytes(seed)
    intermediate_decode: bytes = check_decode(intermediate_passphrase)
    if len(intermediate_decode) != 49:
        raise ValueError(f"Invalid intermediate passphrase length (expected 49, got {len(intermediate_decode)!r})")

    magic: bytes = intermediate_decode[:8]
    owner_entropy: bytes = intermediate_decode[8:16]
    pass_point: bytes = intermediate_decode[16:]

    if magic == integer_to_bytes(MAGIC_LOT_AND_SEQUENCE):
        if public_key_type == "uncompressed":
            flag: bytes = integer_to_bytes(MAGIC_LOT_AND_SEQUENCE_UNCOMPRESSED_FLAG)
        elif public_key_type == "compressed":
            flag: bytes = integer_to_bytes(MAGIC_LOT_AND_SEQUENCE_COMPRESSED_FLAG)
        else:
            raise ValueError(f"Invalid public key type (expected uncompressed/compressed, got {public_key_type!r})")
    elif magic == integer_to_bytes(MAGIC_NO_LOT_AND_SEQUENCE):
        if public_key_type == "uncompressed":
            flag: bytes = integer_to_bytes(MAGIC_NO_LOT_AND_SEQUENCE_UNCOMPRESSED_FLAG)
        elif public_key_type == "compressed":
            flag: bytes = integer_to_bytes(MAGIC_NO_LOT_AND_SEQUENCE_COMPRESSED_FLAG)
        else:
            raise ValueError(f"Invalid public key type (expected uncompressed/compressed, got {public_key_type!r})")
    else:
        raise ValueError(
            f"Invalid magic (expected {bytes_to_string(integer_to_bytes(MAGIC_LOT_AND_SEQUENCE))!r}/"
            f"{bytes_to_string(integer_to_bytes(MAGIC_NO_LOT_AND_SEQUENCE))!r}, got {bytes_to_string(magic)!r})"
        )

    factor_b: bytes = double_sha256(seed_b)
    if not 0 < bytes_to_integer(factor_b) < N:
        raise ValueError("Invalid ec encrypted wallet important format")

    public_key: bytes = multiply_public_key(pass_point, factor_b, public_key_type)
    address: str = public_key_to_addresses(public_key=public_key, network=network)
    address_hash: bytes = get_checksum(get_bytes(address, unhexlify=False))
    salt: bytes = address_hash + owner_entropy
    scrypt_hash: bytes = scrypt.hash(pass_point, salt, 1024, 1, 1, 64)
    derived_half_1, derived_half_2, key = scrypt_hash[:16], scrypt_hash[16:32], scrypt_hash[32:]

    aes: AESModeOfOperationECB = AESModeOfOperationECB(key)
    encrypted_half_1: bytes = aes.encrypt(integer_to_bytes(
        bytes_to_integer(seed_b[:16]) ^ bytes_to_integer(derived_half_1)
    ))
    encrypted_half_2: bytes = aes.encrypt(integer_to_bytes(
        bytes_to_integer(encrypted_half_1[8:] + seed_b[16:]) ^ bytes_to_integer(derived_half_2)
    ))
    encrypted_wif: str = ensure_string(check_encode((
        integer_to_bytes(BIP38_EC_MULTIPLIED_PRIVATE_KEY_PREFIX) + flag + address_hash + owner_entropy + encrypted_half_1[:8] + encrypted_half_2
    )))

    point_b: bytes = get_bytes(private_key_to_public_key(factor_b, public_key_type="compressed"))
    point_b_prefix: bytes = integer_to_bytes(
        (bytes_to_integer(scrypt_hash[63:]) & 1) ^ bytes_to_integer(point_b[:1])
    )
    point_b_half_1: bytes = aes.encrypt(integer_to_bytes(
        bytes_to_integer(point_b[1:17]) ^ bytes_to_integer(derived_half_1)
    ))
    point_b_half_2: bytes = aes.encrypt(integer_to_bytes(
        bytes_to_integer(point_b[17:]) ^ bytes_to_integer(derived_half_2)
    ))
    encrypted_point_b: bytes = (
        point_b_prefix + point_b_half_1 + point_b_half_2
    )
    confirmation_code: str = ensure_string(check_encode((
        integer_to_bytes(CONFIRMATION_CODE_PREFIX) + flag + address_hash + owner_entropy + encrypted_point_b
    )))

    return dict(
        encrypted_wif=encrypted_wif,
        confirmation_code=confirmation_code,
        public_key=bytes_to_string(public_key),
        seed=bytes_to_string(seed_b),
        public_key_type=public_key_type,
        address=address
    )


def confirm_code(
    passphrase: str, confirmation_code: str, network: Literal["mainnet", "testnet"] = "mainnet", detail: bool = False
) -> Union[str, dict]:
    """
    Confirm passphrase

    :param passphrase: Passphrase or password text
    :type passphrase: str
    :param confirmation_code: Confirmation code
    :type confirmation_code: str
    :param network: Network type
    :type network: Literal["mainnet", "testnet"], default to ``mainnet``
    :param detail: To show in detail, default to ``False``
    :type detail: bool

    :returns: Union[str, dict] -- Confirmation of address info's

    >>> from bip38 import confirm_code
    >>> confirm_code(passphrase="TestingOneTwoThree", confirmation_code="cfrm38V8Foq3WpRPMXJD34SF6pGT6ht5ihYMWWMbezkzHgPpA1jVkfbTHwQzvuSA4ReF86PHZJY")
    '1JbyXoVN4hXWirGB265q9VE4pQ6qbY6kmr'
    >>> confirm_code(passphrase="TestingOneTwoThree", confirmation_code="cfrm38VXL5T6qVke13sHUWtEjibAkK1RquBqMXb2azCv1Zna6JKvBhD1Gf2b15wBj7UPv2BQnf6", detail=True)
    {'public_key': '02100bb0440ff4106a1743750813271e66a7017431e92921e520319f537c7357c1', 'public_key_type': 'compressed', 'address': '15PuNwFmDqYhRsC9MDPNFvNY4Npzibm67c', 'lot': 199999, 'sequence': 1}
    """

    confirmation_code_decode: bytes = check_decode(confirmation_code)
    if len(confirmation_code_decode) != 51:
        raise ValueError(f"Invalid confirmation code length (expected 102, got {len(confirmation_code_decode)!r})")

    prefix_length: int = len(integer_to_bytes(CONFIRMATION_CODE_PREFIX))
    prefix_got: bytes = confirmation_code_decode[:prefix_length]
    if integer_to_bytes(CONFIRMATION_CODE_PREFIX) != prefix_got:
        raise ValueError(f"Invalid confirmation code prefix (expected {prefix_length!r}, got {prefix_got!r})")

    flag: bytes = confirmation_code_decode[5:6]
    address_hash: bytes = confirmation_code_decode[6:10]
    owner_entropy: bytes = confirmation_code_decode[10:18]
    encrypted_point_b: bytes = confirmation_code_decode[18:]

    lot_and_sequence: Optional[bytes] = None
    if bytes_to_integer(flag) in FLAGS["lot_and_sequence"]:
        owner_salt: bytes = owner_entropy[:4]
        lot_and_sequence = owner_entropy[4:]
    else:
        owner_salt: bytes = owner_entropy

    pass_factor: bytes = scrypt.hash(unicodedata.normalize("NFC", passphrase), owner_salt, 16384, 8, 8, 32)
    if lot_and_sequence:
        pass_factor: bytes = double_sha256(pass_factor + owner_entropy)
    if bytes_to_integer(pass_factor) == 0 or bytes_to_integer(pass_factor) >= N:
        raise ValueError("Invalid ec encrypted wallet important format")

    pass_point: str = private_key_to_public_key(
        private_key=pass_factor, public_key_type="compressed"
    )
    salt: bytes = address_hash + owner_entropy
    scrypt_hash: bytes = scrypt.hash(get_bytes(pass_point), salt, 1024, 1, 1, 64)
    derived_half_1, derived_half_2, key = encrypted_point_b[1:17], encrypted_point_b[17:], scrypt_hash[32:]

    aes: AESModeOfOperationECB = AESModeOfOperationECB(key)
    point_b_half_1: bytes = integer_to_bytes(
        bytes_to_integer(aes.decrypt(derived_half_1)) ^ bytes_to_integer(scrypt_hash[:16])
    )
    point_b_half_2: bytes = integer_to_bytes(
        bytes_to_integer(aes.decrypt(derived_half_2)) ^ bytes_to_integer(scrypt_hash[16:32])
    )
    point_b_prefix: bytes = integer_to_bytes(
        bytes_to_integer(encrypted_point_b[:1]) ^ (bytes_to_integer(scrypt_hash[63:]) & 1)
    )
    point_b: bytes = (
        point_b_prefix + point_b_half_1 + point_b_half_2
    )
    public_key: bytes = multiply_public_key(
        public_key=point_b, private_key=pass_factor, public_key_type="uncompressed"
    )
    public_key_type: Literal["uncompressed", "compressed"] = "uncompressed"

    if bytes_to_integer(flag) in FLAGS["compression"]:
        public_key: bytes = get_bytes(compress_public_key(public_key=public_key))
        public_key_type: str = "compressed"

    address: str = public_key_to_addresses(public_key=public_key, network=network)
    if get_checksum(get_bytes(address, unhexlify=False)) == address_hash:
        lot: Optional[int] = None
        sequence: Optional[int] = None
        if detail:
            if lot_and_sequence:
                sequence: int = bytes_to_integer(lot_and_sequence) % 4096
                lot: int = (bytes_to_integer(lot_and_sequence) - sequence) // 4096
            return dict(
                public_key=bytes_to_string(public_key),
                public_key_type=public_key_type,
                address=address,
                lot=lot,
                sequence=sequence
            )
        return address
    raise ValueError("Incorrect passphrase/password")


def bip38_decrypt(
    encrypted_wif: str, passphrase: str, network: Literal["mainnet", "testnet"] = "mainnet", detail: bool = False
) -> Union[str, dict]:
    """
    BIP38 Decrypt encrypted wallet important format using passphrase/password

    :param encrypted_wif: Encrypted wallet important format
    :type encrypted_wif: str
    :param passphrase: Passphrase or password text
    :type passphrase: str
    :param network: Network type
    :type network: Literal["mainnet", "testnet"], default to ``mainnet``
    :param detail: To show in detail, default to ``False``
    :type detail: bool

    :returns: Union[str, dict] -- WIF or All private Key info's

    >>> from bip38 import bip38_decrypt
    >>> bip38_decrypt(encrypted_wif="6PRVWUbkzzsbcVac2qwfssoUJAN1Xhrg6bNk8J7Nzm5H7kxEbn2Nh2ZoGg", passphrase="TestingOneTwoThree")
    '5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR'
    >>> bip38_decrypt(encrypted_wif="6PRVWUbkzzsbcVac2qwfssoUJAN1Xhrg6bNk8J7Nzm5H7kxEbn2Nh2ZoGg", passphrase="TestingOneTwoThree", detail=True)
    {'wif': '5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR', 'private_key': 'cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5', 'wif_type': 'wif', 'public_key': '04d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360ea7f23327b49ba7f10d17fad15f068b8807dbbc9e4ace5d4a0b40264eefaf31a4', 'public_key_type': 'uncompressed', 'address': '1Jq6MksXQVWzrznvZzxkV6oY57oWXD9TXB', 'lot': None, 'sequence': None}
    """

    encrypted_wif_decode: bytes = decode(encrypted_wif)
    if len(encrypted_wif_decode) != 43:
        raise ValueError(f"Invalid encrypted WIF length (expected 43, got {len(encrypted_wif_decode)!r})")

    prefix: bytes = encrypted_wif_decode[:2]
    flag: bytes = encrypted_wif_decode[2:3]
    address_hash: bytes = encrypted_wif_decode[3:7]

    if prefix == integer_to_bytes(BIP38_NO_EC_MULTIPLIED_PRIVATE_KEY_PREFIX):

        if flag == integer_to_bytes(BIP38_NO_EC_MULTIPLIED_WIF_FLAG):
            wif_type: Literal["wif", "wif-compressed"] = "wif"
            public_key_type: Literal["uncompressed", "compressed"] = "uncompressed"
        elif flag == integer_to_bytes(BIP38_NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG):
            wif_type: Literal["wif", "wif-compressed"] = "wif-compressed"
            public_key_type: Literal["uncompressed", "compressed"] = "compressed"
        else:
            raise ValueError(
                f"Invalid flag (expected {bytes_to_string(integer_to_bytes(BIP38_NO_EC_MULTIPLIED_WIF_FLAG))!r}/"
                f"{bytes_to_string(integer_to_bytes(BIP38_NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG))!r}, got {bytes_to_string(flag)!r})"
            )

        key: bytes = scrypt.hash(unicodedata.normalize("NFC", passphrase), address_hash, 16384, 8, 8)
        derived_half_1, derived_half_2 = key[0:32], key[32:64]
        encrypted_half_1: bytes = encrypted_wif_decode[7:23]
        encrypted_half_2: bytes = encrypted_wif_decode[23:39]

        aes: AESModeOfOperationECB = AESModeOfOperationECB(derived_half_2)
        decrypted_half_2: bytes = aes.decrypt(encrypted_half_2)
        decrypted_half_1: bytes = aes.decrypt(encrypted_half_1)

        private_key: bytes = integer_to_bytes(
            bytes_to_integer(decrypted_half_1 + decrypted_half_2) ^ bytes_to_integer(derived_half_1)
        )
        if bytes_to_integer(private_key) == 0 or bytes_to_integer(private_key) >= N:
            raise ValueError("Invalid non-ec encrypted wallet important format")

        public_key: str = private_key_to_public_key(
            private_key=private_key, public_key_type=public_key_type
        )
        address: str = public_key_to_addresses(public_key=public_key, network=network)
        if get_checksum(get_bytes(address, unhexlify=False)) != address_hash:
            raise ValueError("Incorrect passphrase/password")

        wif: str = private_key_to_wif(
            private_key=private_key, wif_type=wif_type
        )
        if detail:
            return dict(
                wif=wif,
                private_key=bytes_to_string(private_key),
                wif_type=wif_type,
                public_key=public_key,
                public_key_type=public_key_type,
                seed=None,
                address=address,
                lot=None,
                sequence=None
            )
        return wif

    elif prefix == integer_to_bytes(BIP38_EC_MULTIPLIED_PRIVATE_KEY_PREFIX):
        owner_entropy: bytes = encrypted_wif_decode[7:15]
        encrypted_half_1_half_1: bytes = encrypted_wif_decode[15:23]
        encrypted_half_2: bytes = encrypted_wif_decode[23:-4]

        lot_and_sequence: Optional[bytes] = None
        if bytes_to_integer(flag) in FLAGS["lot_and_sequence"]:
            owner_salt: bytes = owner_entropy[:4]
            lot_and_sequence = owner_entropy[4:]
        else:
            owner_salt: bytes = owner_entropy

        pass_factor: bytes = scrypt.hash(unicodedata.normalize("NFC", passphrase), owner_salt, 16384, 8, 8, 32)
        if lot_and_sequence:
            pass_factor: bytes = double_sha256(pass_factor + owner_entropy)
        if bytes_to_integer(pass_factor) == 0 or bytes_to_integer(pass_factor) >= N:
            raise ValueError("Invalid ec encrypted wallet important format")

        pre_public_key: str = private_key_to_public_key(
            private_key=pass_factor, public_key_type="compressed"
        )
        salt = address_hash + owner_entropy
        encrypted_seed_b: bytes = scrypt.hash(get_bytes(pre_public_key), salt, 1024, 1, 1, 64)
        key: bytes = encrypted_seed_b[32:]

        aes: AESModeOfOperationECB = AESModeOfOperationECB(key)
        encrypted_half_1_half_2_seed_b_last_3 = integer_to_bytes(
            bytes_to_integer(aes.decrypt(encrypted_half_2)) ^ bytes_to_integer(encrypted_seed_b[16:32])
        )
        encrypted_half_1_half_2: bytes = encrypted_half_1_half_2_seed_b_last_3[:8]
        encrypted_half_1: bytes = (
            encrypted_half_1_half_1 + encrypted_half_1_half_2
        )

        seed_b: bytes = integer_to_bytes(
            bytes_to_integer(aes.decrypt(encrypted_half_1)) ^ bytes_to_integer(encrypted_seed_b[:16])
        ) + encrypted_half_1_half_2_seed_b_last_3[8:]

        factor_b: bytes = double_sha256(seed_b)
        if bytes_to_integer(factor_b) == 0 or bytes_to_integer(factor_b) >= N:
            raise ValueError("Invalid ec encrypted wallet important format")

        private_key: bytes = multiply_private_key(pass_factor, factor_b)
        public_key: str = private_key_to_public_key(
            private_key=private_key, public_key_type="uncompressed"
        )
        wif_type: Literal["wif", "wif-compressed"] = "wif"
        public_key_type: Literal["uncompressed", "compressed"] = "uncompressed"
        if bytes_to_integer(flag) in FLAGS["compression"]:
            public_key: str = compress_public_key(public_key=public_key)
            public_key_type = "compressed"
            wif_type = "wif-compressed"

        address: str = public_key_to_addresses(public_key=public_key, network=network)
        if get_checksum(get_bytes(address, unhexlify=False)) == address_hash:
            wif: str = private_key_to_wif(
                private_key=private_key, wif_type=wif_type
            )
            lot: Optional[int] = None
            sequence: Optional[int] = None
            if detail:
                if lot_and_sequence:
                    sequence: int = bytes_to_integer(lot_and_sequence) % 4096
                    lot: int = (bytes_to_integer(lot_and_sequence) - sequence) // 4096
                return dict(
                    wif=wif,
                    private_key=bytes_to_string(private_key),
                    wif_type=wif_type,
                    public_key=public_key,
                    public_key_type=public_key_type,
                    seed=bytes_to_string(seed_b),
                    address=address,
                    lot=lot,
                    sequence=sequence
                )
            return wif
        raise ValueError("Incorrect passphrase/password")
    else:
        raise ValueError(
            f"Invalid prefix (expected {bytes_to_string(integer_to_bytes(BIP38_NO_EC_MULTIPLIED_PRIVATE_KEY_PREFIX))!r}/"
            f"{bytes_to_string(integer_to_bytes(BIP38_EC_MULTIPLIED_PRIVATE_KEY_PREFIX))!r}, got {bytes_to_string(prefix)!r})"
        )
