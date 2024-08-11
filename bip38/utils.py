#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    AnyStr, Optional, Union, Literal
)


def get_bytes(data: AnyStr, unhexlify: bool = True) -> bytes:
    """
    Convert input data to bytes format.

    :param data: The input data to convert. Can be bytes or string.
    :type data: Union[bytes, str]
    :param unhexlify: Flag indicating whether to interpret strings as hexadecimal (default True).
    :type unhexlify: bool

    :return: The input data converted to bytes format.
    :rtype: bytes
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
    """
    Reverse the order of bytes in a bytes object.

    :param data: The bytes object to reverse.
    :type data: bytes

    :return: The bytes object with its byte order reversed.
    :rtype: bytes
    """

    tmp = bytearray(data)
    tmp.reverse()
    return bytes(tmp)


def bytes_to_string(data: Union[bytes, str]) -> str:
    """
    Convert bytes or string data to a hexadecimal string representation.

    :param data: The bytes or string data to convert to hexadecimal string.
    :type data: Union[bytes, str]

    :return: The hexadecimal string representation of the input data.
    :rtype: str
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
    Convert bytes to an integer based on specified endianness and signedness.

    :param data: The bytes object to convert to an integer.
    :type data: bytes
    :param endianness: The byte order ("little" or "big").
    :type endianness: Literal["little", "big"]
    :param signed: Flag indicating whether the integer is signed (default False).
    :type signed: bool

    :return: The integer value converted from bytes.
    :rtype: int
    """

    return int.from_bytes(data, byteorder=endianness, signed=signed)


def integer_to_bytes(
    data: int, bytes_num: Optional[int] = None, endianness: Literal["little", "big"] = "big", signed: bool = False
) -> bytes:
    """
    Convert an integer to bytes based on specified parameters.

    :param data: The integer to convert to bytes.
    :type data: int
    :param bytes_num: Optional number of bytes to use for the conversion. If not provided, it is calculated based on the integer's bit length.
    :type bytes_num: Optional[int]
    :param endianness: The byte order ("little" or "big").
    :type endianness: Literal["little", "big"]
    :param signed: Flag indicating whether the integer is signed (default False).
    :type signed: bool

    :return: The bytes object representing the integer.
    :rtype: bytes
    """

    bytes_num = bytes_num or ((data.bit_length() if data > 0 else 1) + 7) // 8
    return data.to_bytes(bytes_num, byteorder=endianness, signed=signed)
