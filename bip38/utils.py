#!/usr/bin/env python3

# Copyright © 2023, Meheret Tesfaye Batu <meherett.batu@gmail.com> or <meherett@qtum.info>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    AnyStr, Optional, Union, Literal
)

import hashlib

from .libs.ripemd160 import ripemd160 as r160


def get_bytes(data: AnyStr, unhexlify: bool = True) -> bytes:
    """
    Any string to bytes converter

    :param data: Data
    :type data: AnyStr
    :param unhexlify: Unhexlify, default to ``True``
    :type unhexlify: bool

    :returns: bytes -- Data
    """

    if not data:
        return b''
    if isinstance(data, bytes):
        return data
    elif isinstance(data, str):
        if unhexlify:
            return bytes.fromhex(data)
        else:
            return bytes(data, 'utf-8')
    else:
        raise TypeError("Agreement must be either 'bytes' or 'string'!")


def bytes_reverse(data: bytes) -> bytes:
    tmp = bytearray(data)
    tmp.reverse()
    return bytes(tmp)


def bytes_to_string(data: bytes) -> str:
    """
    Bytes to string converter

    :param data: Data
    :type data: bytes

    :returns: str -- Data
    """

    if not data:
        return ''
    try:
        bytes.fromhex(data)
        return data
    except (ValueError, TypeError):
        pass
    if not isinstance(data, bytes):
        data = bytes(data, 'utf-8')
    return data.hex()


def bytes_to_integer(data: bytes, endianness: Literal["little", "big"] = "big", signed: bool = False) -> int:
    """
    Bytes to integer converter

    :param data: Data
    :type data: bytes
    :param endianness: Endianness, default to ``big``
    :type endianness: Literal["little", "big"]
    :param signed: Signed, default to ``False``
    :type signed: bool

    :returns: int -- Data
    """

    return int.from_bytes(data, byteorder=endianness, signed=signed)


def integer_to_bytes(data: int, bytes_num: Optional[int] = None, endianness: Literal["little", "big"] = "big", signed: bool = False) -> bytes:
    """
    Integer to bytes converter

    :param data: Data
    :type data: int
    :param bytes_num: Bytes number, default to ``None``
    :type bytes_num: Optional[int]
    :param endianness: Endianness, default to ``big``
    :type endianness: Literal["little", "big"]
    :param signed: Signed, default to ``False``
    :type signed: bool

    :returns: bytes -- Data
    """

    bytes_num = bytes_num or ((data.bit_length() if data > 0 else 1) + 7) // 8
    return data.to_bytes(bytes_num, byteorder=endianness, signed=signed)


def ripemd160(data: Union[str, bytes]) -> bytes:
    """
    Ripemd160 hash

    :param data: Data
    :type data: Union[str, bytes]

    :returns: bytes -- Data ripemd160 hash
    """

    return (
        hashlib.new("ripemd160", get_bytes(data)).digest() if "ripemd160" in hashlib.algorithms_available else r160(get_bytes(data))
    )


def sha256(data: Union[str, bytes]) -> bytes:
    """
    SHA256 hash

    :param data: Data
    :type data: Union[str, bytes]

    :returns: bytes -- Data sha256 hash
    """

    return hashlib.sha256(get_bytes(data)).digest()


def double_sha256(data: Union[str, bytes]) -> bytes:
    """
    Double SHA256 hash

    :param data: Data
    :type data: Union[str, bytes]

    :returns: bytes -- Data double sha256 hash
    """

    return hashlib.sha256(sha256(data)).digest()


def hash160(data: Union[str, bytes]) -> bytes:
    """
    Hash160 hash

    :param data: Data
    :type data: Union[str, bytes]

    :returns: bytes -- Data hash160 hash
    """

    return ripemd160(sha256(data))
