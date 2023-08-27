#!/usr/bin/env python3

from typing import (
    AnyStr, Optional, Union
)

import hashlib
import unicodedata

from .libs.ripemd160 import ripemd160 as r160

try:
    from typing import Literal  # pylint: disable=unused-import
except ImportError:
    # Literal not supported by Python 3.7
    from typing_extensions import Literal  # type: ignore # noqa: F401


def get_hex_string(data: AnyStr):

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


def get_bytes(data: AnyStr, unhexlify: bool = True) -> bytes:

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


def bytes_to_integer(data: bytes, endianness: Literal["little", "big"] = "big", signed: bool = False) -> int:
    return int.from_bytes(data, byteorder=endianness, signed=signed)


def integer_to_bytes(data: int, bytes_num: Optional[int] = None, endianness: Literal["little", "big"] = "big", signed: bool = False) -> bytes:
    bytes_num = bytes_num or ((data.bit_length() if data > 0 else 1) + 7) // 8
    return data.to_bytes(bytes_num, byteorder=endianness, signed=signed)


def ripemd160(data: Union[str, bytes]) -> bytes:
    return (
        hashlib.new("ripemd160", get_bytes(data)).digest() if "ripemd160" in hashlib.algorithms_available else r160(get_bytes(data))
    )


def sha256(data: Union[str, bytes]) -> bytes:
    return hashlib.sha256(get_bytes(data)).digest()


def double_sha256(data: Union[str, bytes]) -> bytes:
    return hashlib.sha256(sha256(data)).digest()


def hash160(data: Union[str, bytes]) -> bytes:
    return ripemd160(sha256(data))
