#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Type, Union, Optional, Literal
)
from pyaes import AESModeOfOperationECB

import scrypt
import unicodedata
import os

from .cryptocurrencies import (
    ICryptocurrency, Bitcoin
)
from .libs.base58 import (
    encode, check_encode, decode, check_decode, ensure_string
)
from .secp256k1 import (
    PublicKey, PrivateKey
)
from .p2pkh_address import P2PKHAddress
from .crypto import (
    double_sha256, get_checksum
)
from .utils import (
    integer_to_bytes, bytes_to_integer, bytes_to_string, get_bytes
)
from .const import (
    N,
    MAGIC_LOT_AND_SEQUENCE,
    MAGIC_NO_LOT_AND_SEQUENCE,
    NO_EC_MULTIPLIED_WIF_FLAG,
    NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG,
    NO_EC_MULTIPLIED_PRIVATE_KEY_PREFIX,
    MAGIC_LOT_AND_SEQUENCE_UNCOMPRESSED_FLAG,
    MAGIC_LOT_AND_SEQUENCE_COMPRESSED_FLAG,
    MAGIC_NO_LOT_AND_SEQUENCE_UNCOMPRESSED_FLAG,
    MAGIC_NO_LOT_AND_SEQUENCE_COMPRESSED_FLAG,
    EC_MULTIPLIED_PRIVATE_KEY_PREFIX,
    CONFIRMATION_CODE_PREFIX,
    FLAGS
)
from .wif import (
    private_key_to_wif, wif_to_private_key, get_wif_type
)


class BIP38:
    """
    A class for BIP38 encryption and decryption of Wallet Import Format (WIF) keys.

    :param cryptocurrency: The cryptocurrency class to use (e.g., Bitcoin).
    :type cryptocurrency: Type[ICryptocurrency]
    :param network: The network for the WIF key (e.g., 'mainnet' or 'testnet'). Defaults to 'mainnet'.
    :type network: str
    """

    network: str
    cryptocurrency: Type[ICryptocurrency]
    alphabet: str

    def __init__(
        self, cryptocurrency: Type[ICryptocurrency], network: str = "mainnet"
    ) -> None:

        self.network = network
        self.cryptocurrency = cryptocurrency
        self.alphabet = (
            self.cryptocurrency.ALPHABET
            if self.cryptocurrency.ALPHABET else
            Bitcoin.ALPHABET
        )

    @classmethod
    def intermediate_code(
        cls,
        passphrase: str,
        lot: Optional[int] = None,
        sequence: Optional[int] = None,
        owner_salt: Optional[Union[str, bytes]] = None
    ) -> str:
        """
        Generates an intermediate passphrase.

        :param passphrase: The passphrase or password.
        :type passphrase: str
        :param lot: Optional lot number (100000-999999).
        :type lot: Optional[int]
        :param sequence: Optional sequence number (0-4095).
        :type sequence: Optional[int]
        :param owner_salt: Optional owner salt (default: random 8 bytes).
        :type owner_salt: Optional[str, bytes]

        :returns: The intermediate passphrase.
        :rtype: str

        >>> from bip38 import BIP38
        >>> from bip38.cryptocurrencies import Bitcoin
        >>> bip38: BIP38 = BIP38(cryptocurrency=Bitcoin, network="mainnet")
        >>> bip38.intermediate_code(passphrase="TestingOneTwoThree")
        'passphraseqVKbgU4mWMakKGgCtaeVWoETQdzMBy5696bG2w7ckVBeQmoLhMF9vLaxhmzhT3'
        >>> bip38.intermediate_code(passphrase="TestingOneTwoThree", lot=199999, sequence=1, owner_salt="75ed1cdeb254cb38")
        'passphraseb7ruSN4At4Rb8hPTNcAVezfsjonvUs4Qo3xSp1fBFsFPvVGSbpP2WTJMhw3mVZ'
        """

        owner_salt: bytes = get_bytes(owner_salt) if owner_salt else os.urandom(8)
        if len(owner_salt) not in [4, 8]:
            raise ValueError(f"Invalid owner salt length (expected: 8 or 16, got: {len(bytes_to_string(owner_salt))})")
        if len(owner_salt) == 4 and (not lot or not sequence):
            raise ValueError(
                f"Invalid owner salt length for non lot/sequence (expected: 16, got: {len(bytes_to_string(owner_salt))})")
        if (lot and not sequence) or (not lot and sequence):
            raise ValueError(f"Both lot & sequence are required, got: (lot {lot}) (sequence {sequence})")

        if lot and sequence:
            lot, sequence = int(lot), int(sequence)
            if not 100000 <= lot <= 999999:
                raise ValueError(f"Invalid lot, (expected: 100000 <= lot <= 999999, got: {lot})")
            if not 0 <= sequence <= 4095:
                raise ValueError(f"Invalid lot, (expected: 0 <= sequence <= 4095, got: {sequence})")

            pre_factor: bytes = scrypt.hash(unicodedata.normalize("NFC", passphrase), owner_salt[:4], 16384, 8, 8, 32)
            owner_entropy: bytes = owner_salt[:4] + integer_to_bytes((lot * 4096 + sequence), 4)
            pass_factor: bytes = double_sha256(pre_factor + owner_entropy)
            magic: bytes = integer_to_bytes(MAGIC_LOT_AND_SEQUENCE)
        else:
            pass_factor: bytes = scrypt.hash(unicodedata.normalize("NFC", passphrase), owner_salt, 16384, 8, 8, 32)
            magic: bytes = integer_to_bytes(MAGIC_NO_LOT_AND_SEQUENCE)
            owner_entropy: bytes = owner_salt

        pass_point: PublicKey = PrivateKey.from_bytes(
            private_key=pass_factor
        ).public_key()
        return ensure_string(check_encode(
            magic + owner_entropy + pass_point.raw_compressed()
        ))

    def encrypt(self, wif: str, passphrase: str, network: Optional[str] = None) -> str:
        """
        Encrypts a Wallet Import Format (WIF) key using a passphrase with BIP38 encryption.

        :param wif: The WIF key to be encrypted.
        :type wif: str
        :param passphrase: The passphrase for encryption.
        :type passphrase: str
        :param network: Optional network for encryption. Defaults to the class's network if not provided.
        :type network: Optional[str]

        :returns: Encrypted WIF key as a string.
        :rtype: str

        >>> from bip38 import BIP38
        >>> from bip38.cryptocurrencies import Bitcoin
        >>> bip38: BIP38 = BIP38(cryptocurrency=Bitcoin, network="mainnet")
        >>> bip38.encrypt(wif="5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR", passphrase="TestingOneTwoThree")
        '6PRVWUbkzzsbcVac2qwfssoUJAN1Xhrg6bNk8J7Nzm5H7kxEbn2Nh2ZoGg'
        >>> bip38.encrypt(wif="L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP", passphrase="TestingOneTwoThree")
        '6PYNKZ1EAgYgmQfmNVamxyXVWHzK5s6DGhwP4J5o44cvXdoY7sRzhtpUeo'
        >>> bip38.encrypt(wif="938jwjergAxARSWx2YSt9nSBWBz24h8gLhv7EUfgEP1wpMLg6iX", passphrase="TestingOneTwoThree", network="testnet")
        '6PRL8jj6dLQjBBJjHMdUKLSNLEpjTyAfmt8GnCnfT87NeQ2BU5eAW1tcsS'
        >>> bip38.encrypt(wif="cURAYbG6FtvUasdBsooEmmY9MqUfhJ8tdybQWV7iA4BAwunCT2Fu", passphrase="TestingOneTwoThree", network="testnet")
        '6PYVB5nHnumbUua1UmsAMPHWHa76Ci48MY79aKYnpKmwxeGqHU2XpXtKvo'
        """

        network: str = (
            network if network else self.network
        )
        wif_type: str = get_wif_type(
            wif=wif, cryptocurrency=self.cryptocurrency, network=network
        )
        if wif_type == "wif":
            flag: bytes = integer_to_bytes(NO_EC_MULTIPLIED_WIF_FLAG)
            private_key: PrivateKey = PrivateKey.from_bytes(get_bytes(wif_to_private_key(
                wif=wif, cryptocurrency=self.cryptocurrency, network=network
            )))
            public_key_type: str = "uncompressed"
        elif wif_type == "wif-compressed":
            flag: bytes = integer_to_bytes(NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG)
            private_key: PrivateKey = PrivateKey.from_bytes(get_bytes(wif_to_private_key(
                wif=wif, cryptocurrency=self.cryptocurrency, network=network
            )))
            public_key_type: str = "compressed"
        else:
            raise ValueError("Wrong WIF (Wallet Important Format) type")

        address: str = P2PKHAddress.encode(
            public_key=private_key.public_key(),
            address_prefix=self.cryptocurrency.NETWORKS[network]["address_prefix"],
            public_key_type=public_key_type
        )
        address_hash: bytes = get_checksum(get_bytes(address, unhexlify=False))
        key: bytes = scrypt.hash(unicodedata.normalize("NFC", passphrase), address_hash, 16384, 8, 8)
        derived_half_1, derived_half_2 = key[0:32], key[32:64]

        aes: AESModeOfOperationECB = AESModeOfOperationECB(derived_half_2)
        encrypted_half_1: bytes = aes.encrypt(integer_to_bytes(
            bytes_to_integer(private_key.raw()[0:16]) ^ bytes_to_integer(derived_half_1[0:16])
        ))
        encrypted_half_2: bytes = aes.encrypt(integer_to_bytes(
            bytes_to_integer(private_key.raw()[16:32]) ^ bytes_to_integer(derived_half_1[16:32])
        ))

        encrypted_private_key: bytes = (
            integer_to_bytes(
                NO_EC_MULTIPLIED_PRIVATE_KEY_PREFIX
            ) + flag + address_hash + encrypted_half_1 + encrypted_half_2
        )
        return ensure_string(encode(
            encrypted_private_key + get_checksum(encrypted_private_key)
        ))

    def create_new_encrypted_wif(
        self,
        intermediate_passphrase: str,
        public_key_type: str = "uncompressed",
        seed: Optional[Union[str, bytes]] = None,
        network: Optional[str] = None
    ) -> dict:
        """
        Creates a new encrypted WIF (Wallet Import Format).

        :param intermediate_passphrase: The intermediate passphrase.
        :type intermediate_passphrase: str
        :param public_key_type: The type of public key (default: "uncompressed").
        :type public_key_type: str
        :param seed: Optional seed (default: random 24 bytes).
        :type seed: Optional[str, bytes]
        :param network: Optional network for encryption. Defaults to the class's network if not provided.
        :type network: Optional[str]

        :returns: A dictionary containing the encrypted WIF.
        :rtype: dict

        >>> from bip38 import BIP38
        >>> from bip38.cryptocurrencies import Bitcoin
        >>> bip38: BIP38 = BIP38(cryptocurrency=Bitcoin, network="testnet")
        >>> bip38.create_new_encrypted_wif(intermediate_passphrase="passphraseb7ruSN4At4Rb8hPTNcAVezfsjonvUs4Qo3xSp1fBFsFPvVGSbpP2WTJMhw3mVZ", public_key_type="uncompressed")
        {'encrypted_wif': '6PgMqfwt1nqJeUkCTRVf4TV6FJoqA8GFCGaj6RsTW1t3XgQNUDfKW9u9Px', 'confirmation_code': 'cfrm38V8ZR17HkU8Xdu8RunWf8CZauXphNQa5HFJd4cxEYckXHS6tfo9M73yL3FPmWv1xqBQsgG', 'public_key': '04fdfbd938b4bb220c11fc1c22e87c5306d105130dd05d7ece4013aa1d2382f3a2a8673fd7b4b2f55c48cd0ebda7d88089783b3394210a0853159803b5eb99097e', 'seed': '0a89d39d0af0f0d7abc655baa0e399f8ddcd372bb9aaebce', 'public_key_type': 'uncompressed', 'address': 'myRfjUS74ab2ZbEbQuiWNzPHb5fSYuFvm4'}
        >>> bip38.create_new_encrypted_wif(intermediate_passphrase="passphraseb7ruSN4At4Rb8hPTNcAVezfsjonvUs4Qo3xSp1fBFsFPvVGSbpP2WTJMhw3mVZ", public_key_type="compressed", seed="99241d58245c883896f80843d2846672d7312e6195ca1a6c")
        {'encrypted_wif': '6PoH364JVeoBPsJBveXCwfWpX2H82N5qiAervtynak7r7dzZF2TBFxZAXE', 'confirmation_code': 'cfrm38VX6jSx7C3nbxWCVEdGna7JMpm57zHdbuofbpCA9EiN57aEt4s5fh9k19b5cTmyZ5jMkE2', 'public_key': '02100bb0440ff4106a1743750813271e66a7017431e92921e520319f537c7357c1', 'seed': '99241d58245c883896f80843d2846672d7312e6195ca1a6c', 'public_key_type': 'compressed', 'address': 'mjurfzLk2ryxCyfm4nMk5qarvNRhbNCtK8'}
        """

        seed_b: bytes = get_bytes(seed) if seed else os.urandom(24)
        intermediate_decode: bytes = check_decode(intermediate_passphrase)
        if len(intermediate_decode) != 49:
            raise ValueError(f"Invalid intermediate passphrase length (expected: 49, got: {len(intermediate_decode)})")

        magic: bytes = intermediate_decode[:8]
        owner_entropy: bytes = intermediate_decode[8:16]
        pass_point: bytes = intermediate_decode[16:]

        if magic == integer_to_bytes(MAGIC_LOT_AND_SEQUENCE):
            if public_key_type == "uncompressed":
                flag: bytes = integer_to_bytes(MAGIC_LOT_AND_SEQUENCE_UNCOMPRESSED_FLAG)
            elif public_key_type == "compressed":
                flag: bytes = integer_to_bytes(MAGIC_LOT_AND_SEQUENCE_COMPRESSED_FLAG)
            else:
                raise ValueError(
                    f"Invalid public key type (expected: 'uncompressed' or 'compressed', got: {public_key_type})")
        elif magic == integer_to_bytes(MAGIC_NO_LOT_AND_SEQUENCE):
            if public_key_type == "uncompressed":
                flag: bytes = integer_to_bytes(MAGIC_NO_LOT_AND_SEQUENCE_UNCOMPRESSED_FLAG)
            elif public_key_type == "compressed":
                flag: bytes = integer_to_bytes(MAGIC_NO_LOT_AND_SEQUENCE_COMPRESSED_FLAG)
            else:
                raise ValueError(
                    f"Invalid public key type (expected: 'uncompressed' or 'compressed', got: {public_key_type})")
        else:
            raise ValueError(
                f"Invalid magic (expected: {bytes_to_string(integer_to_bytes(MAGIC_LOT_AND_SEQUENCE))}/"
                f"{bytes_to_string(integer_to_bytes(MAGIC_NO_LOT_AND_SEQUENCE))}, got: {bytes_to_string(magic)})"
            )

        factor_b: bytes = double_sha256(seed_b)
        if not 0 < bytes_to_integer(factor_b) < N:
            raise ValueError("Invalid EC encrypted WIF (Wallet Important Format)")

        public_key: PublicKey = PublicKey.from_point(
            PublicKey.from_bytes(pass_point).point() * bytes_to_integer(factor_b)
        )
        address: str = P2PKHAddress.encode(
            public_key=public_key,
            address_prefix=self.cryptocurrency.NETWORKS[network if network else self.network]["address_prefix"],
            public_key_type=public_key_type
        )
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
            integer_to_bytes(EC_MULTIPLIED_PRIVATE_KEY_PREFIX) +
            flag + address_hash + owner_entropy + encrypted_half_1[:8] + encrypted_half_2
        )))

        point_b: bytes = PrivateKey.from_bytes(factor_b).public_key().raw_compressed()
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
            public_key=bytes_to_string(
                public_key.raw(public_key_type=public_key_type)
            ),
            seed=bytes_to_string(seed_b),
            public_key_type=public_key_type,
            address=address
        )

    def confirm_code(
        self, passphrase: str, confirmation_code: str, network: Optional[str] = None, detail: bool = False
    ) -> Union[str, dict]:
        """
        Confirms the passphrase using a confirmation code.

        :param passphrase: The passphrase or password.
        :type passphrase: str
        :param confirmation_code: The confirmation code.
        :type confirmation_code: str
        :param network: Optional network for encryption. Defaults to the class's network if not provided.
        :type network: Optional[str]
        :param detail: Whether to return detailed info (default: False).
        :type detail: bool

        :returns: Confirmation result as a string or detailed info as a dictionary.
        :rtype: Union[str, dict]

        >>> from bip38 import BIP38
        >>> from bip38.cryptocurrencies import Bitcoin
        >>> bip38: BIP38 = BIP38(cryptocurrency=Bitcoin, network="testnet")
        >>> bip38.confirm_code(passphrase="TestingOneTwoThree", confirmation_code="cfrm38V8ZQSdCuzcrYYKGNXVwbHgdjsUEfAbFGoEUouB4YEKaXVdFiMcBWai1Exdu8jN7DcoKtM")
        'mwW38M23zvDmhbsTdnVFzw3bVnueDhrKec'
        >>> bip38.confirm_code(passphrase="TestingOneTwoThree", confirmation_code="cfrm38V8Foq3WpRPMXJD34SF6pGT6ht5ihYMWWMbezkzHgPpA1jVkfbTHwQzvuSA4ReF86PHZJY", network="mainnet")
        '1JbyXoVN4hXWirGB265q9VE4pQ6qbY6kmr'
        >>> bip38.confirm_code(passphrase="TestingOneTwoThree", confirmation_code="cfrm38VXL5T6qVke13sHUWtEjibAkK1RquBqMXb2azCv1Zna6JKvBhD1Gf2b15wBj7UPv2BQnf6", network="mainnet", detail=True)
        {'public_key': '02100bb0440ff4106a1743750813271e66a7017431e92921e520319f537c7357c1', 'public_key_type': 'compressed', 'address': '15PuNwFmDqYhRsC9MDPNFvNY4Npzibm67c', 'lot': 199999, 'sequence': 1}
        """

        confirmation_code_decode: bytes = check_decode(confirmation_code)
        if len(confirmation_code_decode) != 51:
            raise ValueError(f"Invalid confirmation code length (expected: 102, got: {len(confirmation_code_decode)})")

        prefix_length: int = len(integer_to_bytes(CONFIRMATION_CODE_PREFIX))
        prefix_got: bytes = confirmation_code_decode[:prefix_length]
        if integer_to_bytes(CONFIRMATION_CODE_PREFIX) != prefix_got:
            raise ValueError(f"Invalid confirmation code prefix (expected: {prefix_length}, got: {prefix_got})")

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
            raise ValueError("Invalid EC encrypted WIF (Wallet Important Format)")

        pass_point: bytes = PrivateKey.from_bytes(pass_factor).public_key().raw_compressed()
        salt: bytes = address_hash + owner_entropy
        scrypt_hash: bytes = scrypt.hash(pass_point, salt, 1024, 1, 1, 64)
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
        public_key: PublicKey = PublicKey.from_point(
            PublicKey.from_bytes(point_b).point() * bytes_to_integer(pass_factor)
        )
        public_key_type: str = "uncompressed"
        if bytes_to_integer(flag) in FLAGS["compression"]:
            public_key_type: str = "compressed"

        address: str = P2PKHAddress.encode(
            public_key=public_key,
            address_prefix=self.cryptocurrency.NETWORKS[network if network else self.network]["address_prefix"],
            public_key_type=public_key_type
        )
        if get_checksum(get_bytes(address, unhexlify=False)) == address_hash:
            lot: Optional[int] = None
            sequence: Optional[int] = None
            if detail:
                if lot_and_sequence:
                    sequence: int = bytes_to_integer(lot_and_sequence) % 4096
                    lot: int = (bytes_to_integer(lot_and_sequence) - sequence) // 4096
                return dict(
                    public_key=bytes_to_string(public_key.raw(public_key_type=public_key_type)),
                    public_key_type=public_key_type,
                    address=address,
                    lot=lot,
                    sequence=sequence
                )
            return address
        raise ValueError("Incorrect passphrase or password")

    def decrypt(
        self, encrypted_wif: str, passphrase: str, network: Optional[str] = None, detail: bool = False
    ) -> Union[str, dict]:
        """
        Decrypts an encrypted WIF (Wallet Import Format) using a passphrase.

        :param encrypted_wif: The encrypted WIF.
        :type encrypted_wif: str
        :param passphrase: The passphrase or password.
        :type passphrase: str
        :param network: Optional network for encryption. Defaults to the class's network if not provided.
        :type network: Optional[str]
        :param detail: Whether to return detailed info (default: False).
        :type detail: bool

        :returns: The decrypted WIF or detailed private key info.
        :rtype: Union[str, dict]

        >>> from bip38 import BIP38
        >>> from bip38.cryptocurrencies import Bitcoin
        >>> bip38: BIP38 = BIP38(cryptocurrency=Bitcoin, network="mainnet")
        >>> bip38.decrypt(encrypted_wif="6PRVWUbkzzsbcVac2qwfssoUJAN1Xhrg6bNk8J7Nzm5H7kxEbn2Nh2ZoGg", passphrase="TestingOneTwoThree")
        '5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR'
        >>> bip38.decrypt(encrypted_wif="6PRVWUbkzzsbcVac2qwfssoUJAN1Xhrg6bNk8J7Nzm5H7kxEbn2Nh2ZoGg", passphrase="TestingOneTwoThree", detail=True)
        {'wif': '5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR', 'private_key': 'cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5', 'wif_type': 'wif', 'public_key': '04d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360ea7f23327b49ba7f10d17fad15f068b8807dbbc9e4ace5d4a0b40264eefaf31a4', 'public_key_type': 'uncompressed', 'seed': None, 'address': '1Jq6MksXQVWzrznvZzxkV6oY57oWXD9TXB', 'lot': None, 'sequence': None}
        >>> bip38.decrypt(encrypted_wif="6PRL8jj6dLQjBBJjHMdUKLSNLEpjTyAfmt8GnCnfT87NeQ2BU5eAW1tcsS", passphrase="TestingOneTwoThree", network="testnet")
        '938jwjergAxARSWx2YSt9nSBWBz24h8gLhv7EUfgEP1wpMLg6iX'
        >>> bip38.decrypt(encrypted_wif="6PRL8jj6dLQjBBJjHMdUKLSNLEpjTyAfmt8GnCnfT87NeQ2BU5eAW1tcsS", passphrase="TestingOneTwoThree", network="testnet", detail=True)
        {'wif': '938jwjergAxARSWx2YSt9nSBWBz24h8gLhv7EUfgEP1wpMLg6iX', 'private_key': 'cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5', 'wif_type': 'wif', 'public_key': '04d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360ea7f23327b49ba7f10d17fad15f068b8807dbbc9e4ace5d4a0b40264eefaf31a4', 'public_key_type': 'uncompressed', 'seed': None, 'address': 'myM3eoxWDWxFe7GYHZw8K21rw7QDNZeDYM', 'lot': None, 'sequence': None}
        """

        network: str = (
            network if network else self.network
        )
        encrypted_wif_decode: bytes = decode(encrypted_wif)
        if len(encrypted_wif_decode) != 43:
            raise ValueError(f"Invalid encrypted WIF length (expected: 43, got: {len(encrypted_wif_decode)})")

        prefix: bytes = encrypted_wif_decode[:2]
        flag: bytes = encrypted_wif_decode[2:3]
        address_hash: bytes = encrypted_wif_decode[3:7]

        if prefix == integer_to_bytes(NO_EC_MULTIPLIED_PRIVATE_KEY_PREFIX):

            if flag == integer_to_bytes(NO_EC_MULTIPLIED_WIF_FLAG):
                wif_type: Literal["wif", "wif-compressed"] = "wif"
                public_key_type: str = "uncompressed"
            elif flag == integer_to_bytes(NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG):
                wif_type: Literal["wif", "wif-compressed"] = "wif-compressed"
                public_key_type: str = "compressed"
            else:
                raise ValueError(
                    f"Invalid flag (expected: {bytes_to_string(integer_to_bytes(NO_EC_MULTIPLIED_WIF_FLAG))} or "
                    f"{bytes_to_string(integer_to_bytes(NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG))}, got: {bytes_to_string(flag)})"
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
                raise ValueError("Invalid Non-EC encrypted WIF (Wallet Important Format)")

            public_key: PublicKey = PrivateKey.from_bytes(private_key).public_key()
            address: str = P2PKHAddress.encode(
                public_key=public_key,
                address_prefix=self.cryptocurrency.NETWORKS[network]["address_prefix"],
                public_key_type=public_key_type
            )
            if get_checksum(get_bytes(address, unhexlify=False)) != address_hash:
                raise ValueError("Incorrect passphrase or password")

            wif: str = private_key_to_wif(
                private_key=private_key, wif_type=wif_type, cryptocurrency=self.cryptocurrency, network=network
            )
            if detail:
                return dict(
                    wif=wif,
                    private_key=bytes_to_string(private_key),
                    wif_type=wif_type,
                    public_key=bytes_to_string(public_key.raw(public_key_type=public_key_type)),
                    public_key_type=public_key_type,
                    seed=None,
                    address=address,
                    lot=None,
                    sequence=None
                )
            return wif

        elif prefix == integer_to_bytes(EC_MULTIPLIED_PRIVATE_KEY_PREFIX):
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
                raise ValueError("Invalid EC encrypted WIF (Wallet Important Format)")

            pre_public_key: PublicKey = PrivateKey.from_bytes(pass_factor).public_key()
            salt = address_hash + owner_entropy
            encrypted_seed_b: bytes = scrypt.hash(pre_public_key.raw_compressed(), salt, 1024, 1, 1, 64)
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
                raise ValueError("Invalid EC encrypted WIF (Wallet Important Format)")

            # multiply private key
            private_key: bytes = integer_to_bytes(
                (bytes_to_integer(pass_factor) * bytes_to_integer(factor_b)) % N
            )
            public_key: PublicKey = PrivateKey.from_bytes(private_key).public_key()
            wif_type: Literal["wif", "wif-compressed"] = "wif"
            public_key_type: str = "uncompressed"
            if bytes_to_integer(flag) in FLAGS["compression"]:
                public_key_type = "compressed"
                wif_type = "wif-compressed"
            address: str = P2PKHAddress.encode(
                public_key=public_key,
                address_prefix=self.cryptocurrency.NETWORKS[network]["address_prefix"],
                public_key_type=public_key_type
            )
            if get_checksum(get_bytes(address, unhexlify=False)) == address_hash:
                wif: str = private_key_to_wif(
                    private_key=private_key, wif_type=wif_type, cryptocurrency=self.cryptocurrency, network=network
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
                        public_key=bytes_to_string(public_key.raw(public_key_type=public_key_type)),
                        public_key_type=public_key_type,
                        seed=bytes_to_string(seed_b),
                        address=address,
                        lot=lot,
                        sequence=sequence
                    )
                return wif
            raise ValueError("Incorrect passphrase or password")
        else:
            raise ValueError(
                f"Invalid prefix (expected: {bytes_to_string(integer_to_bytes(NO_EC_MULTIPLIED_PRIVATE_KEY_PREFIX))} or "
                f"{bytes_to_string(integer_to_bytes(EC_MULTIPLIED_PRIVATE_KEY_PREFIX))}, got: {bytes_to_string(prefix)})"
            )
