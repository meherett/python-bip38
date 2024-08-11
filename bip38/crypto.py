#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import Union

import hashlib

from .libs.ripemd160 import ripemd160 as r160
from .const import CHECKSUM_BYTE_LENGTH
from .utils import get_bytes


def ripemd160(data: Union[str, bytes]) -> bytes:
    """
    Calculate the RIPEMD-160 hash of the given data.

    :param data: The data to hash, as bytes or a string.
    :type data: Union[str, bytes]

    :return: The RIPEMD-160 hash digest as bytes.
    :rtype: bytes
    """

    return (
        hashlib.new("ripemd160", get_bytes(data)).digest()
        if "ripemd160" in hashlib.algorithms_available else
        r160(get_bytes(data))
    )


def sha256(data: Union[str, bytes]) -> bytes:
    """
    Calculate the SHA-256 hash of the given data.

    :param data: The data to hash, as bytes or a string.
    :type data: Union[str, bytes]

    :return: The SHA-256 hash digest as bytes.
    :rtype: bytes
    """

    return hashlib.sha256(get_bytes(data)).digest()


def double_sha256(data: Union[str, bytes]) -> bytes:
    """
    Calculate the double SHA-256 hash of the given data.

    :param data: The data to hash, as bytes or a string.
    :type data: Union[str, bytes]

    :return: The double SHA-256 hash digest as bytes.
    :rtype: bytes
    """

    return sha256(sha256(data))


def get_checksum(data: Union[str, bytes]) -> bytes:
    """
    Calculate the checksum for the given raw bytes.

    The checksum is derived by performing a double SHA-256 hash on the input
    and returning the first few bytes, as determined by `CHECKSUM_BYTE_LENGTH`.

    :param data: The raw data to checksum.
    :type data: Union[str, bytes]

    :returns: The checksum of the data.
    :rtype: bytes
    """

    return double_sha256(data)[:CHECKSUM_BYTE_LENGTH]


def hash160(data: Union[str, bytes]) -> bytes:
    """
    Calculate the HASH160 hash (RIPEMD-160 of SHA-256) of the given data.

    :param data: The data to hash, as bytes or a string.
    :type data: Union[str, bytes]

    :return: The HASH160 hash digest as bytes.
    :rtype: bytes
    """

    return ripemd160(sha256(data))
