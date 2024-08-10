#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    List, Dict
)

# non-EC-multiplied & EC-multiplied private key prefixes
NO_EC_MULTIPLIED_PRIVATE_KEY_PREFIX: int = 0x0142
EC_MULTIPLIED_PRIVATE_KEY_PREFIX: int = 0x0143
# non-EC-multiplied Wallet Important Format (WIF) flags
NO_EC_MULTIPLIED_WIF_FLAG: int = 0xc0
NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG: int = 0xe0
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
# Number of points in the field
N: int = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
# Coordinate point length
COORDINATE_POINT_LENGTH: int = 32
# Private key length & prefixes
PRIVATE_KEY_LENGTH: int = 32
UNCOMPRESSED_PRIVATE_KEY_PREFIX: int = 0x00
COMPRESSED_PRIVATE_KEY_PREFIX: int = 0x01
# Public key length & prefixes
COMPRESSED_PUBLIC_KEY_LENGTH: int = 33
UNCOMPRESSED_PUBLIC_KEY_LENGTH: int = 65
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
        NO_EC_MULTIPLIED_WIF_FLAG, NO_EC_MULTIPLIED_WIF_COMPRESSED_FLAG, 0xc8, 0xd0, 0xd8, 0xe8, 0xf0, 0xf8
    ],
    "ec": [
        0x00, 0x04, 0x08, 0x0c, 0x10, 0x14, 0x18, 0x1c, 0x20, 0x24, 0x28, 0x2c, 0x30, 0x34, 0x38, 0x3c
    ],
    "illegal": [
        0xc4, 0xcc, 0xd4, 0xdc, 0xe4, 0xec, 0xf4, 0xfc
    ]
}
