#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import *

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
        MAGIC_NO_LOT_AND_SEQUENCE_COMPRESSED_FLAG, MAGIC_LOT_AND_SEQUENCE_COMPRESSED_FLAG, 0x28, 0x2c, 0x30, 0x34, 0x38, 0x3c, 0xe0, 0xe8, 0xf0, 0xf8
    ],
    "lot_and_sequence": [
        MAGIC_LOT_AND_SEQUENCE_UNCOMPRESSED_FLAG, MAGIC_LOT_AND_SEQUENCE_COMPRESSED_FLAG, 0x0c, 0x14, 0x1c, 0x2c, 0x34, 0x3c
    ],
    "non_ec": [
        BIP38_NO_EC_MULTIPLIED_WIF_FLAG, BIP38_NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG, 0xc8, 0xd0, 0xd8, 0xe8, 0xf0, 0xf8
    ],
    "ec": [
        0x00, 0x04, 0x08, 0x0c, 0x10, 0x14, 0x18, 0x1c, 0x20, 0x24, 0x28, 0x2c, 0x30, 0x34, 0x38, 0x3c
    ],
    "illegal": [
        0xc4, 0xcc, 0xd4, 0xdc, 0xe4, 0xec, 0xf4, 0xfc
    ]
}


class SECP256K1:
    """
    ``SECP256K1`` Constants.

    +-------------------------------------+-------------+
    | Name                                | Value       |
    +=====================================+=============+
    | POINT_COORDINATE_BYTE_LENGTH        | 32          |
    +-------------------------------------+-------------+
    | PRIVATE_KEY_BYTE_LENGTH             | 32          |
    +-------------------------------------+-------------+
    | PUBLIC_KEY_PREFIX                   | ``0x04``    |
    +-------------------------------------+-------------+
    | PUBLIC_KEY_COMPRESSED_BYTE_LENGTH   | 33          |
    +-------------------------------------+-------------+
    | PUBLIC_KEY_UNCOMPRESSED_BYTE_LENGTH | 65          |
    +-------------------------------------+-------------+
    """

    POINT_COORDINATE_BYTE_LENGTH: int = 32
    PRIVATE_KEY_BYTE_LENGTH: int = 32
    PUBLIC_KEY_UNCOMPRESSED_PREFIX: bytes = b"\x04"
    PUBLIC_KEY_COMPRESSED_BYTE_LENGTH: int = 33
    PUBLIC_KEY_UNCOMPRESSED_BYTE_LENGTH: int = 65


class PUBLIC_KEY_TYPES:
    """
    ``PUBLIC_KEY_TYPES`` Constants.

    +----------------+-----------------+
    | Name           | Value           |
    +================+=================+
    | COMPRESSED     | 'uncompressed'  |
    +----------------+-----------------+
    | UNCOMPRESSED   | 'compressed'    |
    +----------------+-----------------+
    """

    UNCOMPRESSED: str = "uncompressed"
    COMPRESSED: str = "compressed"

    @classmethod
    def get_types(cls) -> List[str]:
        """
        Get a list of all public key types.

        :return: List of public key types.
        :rtype: List[str]
        """

        return [
            cls.UNCOMPRESSED, cls.COMPRESSED
        ]


class WIF_TYPES:
    """
    ``WIF_TYPES`` Constants.

    +----------------+------------------+
    | Name           | Value            |
    +================+==================+
    | WIF            | 'wif'            |
    +----------------+------------------+
    | WIF_COMPRESSED | 'wif-compressed' |
    +----------------+------------------+
    """

    WIF: str = "wif"
    WIF_COMPRESSED: str = "wif-compressed"

    @classmethod
    def get_types(cls) -> List[str]:
        """
        Get a list of all WIF types.

        :return: List of WIF types.
        :rtype: List[str]
        """

        return [
            cls.WIF, cls.WIF_COMPRESSED
        ]
