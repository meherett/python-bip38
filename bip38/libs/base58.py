#!/usr/bin/env python3

from binascii import (
    hexlify, unhexlify
)

import hashlib
import six

base58_alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def string_to_int(data):
    val = 0

    if type(data) == str:
        data = bytearray(data)

    for (i, c) in enumerate(data[::-1]):
        val += (256 ** i) * c
    return val


def ensure_string(data):
    if isinstance(data, six.binary_type):
        return data.decode("utf-8")
    elif not isinstance(data, six.string_types):
        raise ValueError("Invalid value for string")
    return data


def encode(data: bytes) -> str:
    """Encode bytes to a base58-encoded string"""

    # Convert big-endian bytes to integer
    n = int('0x0' + hexlify(data).decode('utf8'), 16)

    # Divide that integer into bas58
    res = []
    while n > 0:
        n, r = divmod(n, 58)
        res.append(base58_alphabet[r])
    res = ''.join(res[::-1])

    # Encode leading zeros as base58 zeros
    import sys
    czero = b'\x00'
    if sys.version > '3':
        # In Python3 indexing a bytes returns numbers, not characters.
        czero = 0
    pad = 0
    for c in data:
        if c == czero:
            pad += 1
        else:
            break
    return base58_alphabet[0] * pad + res


def check_encode(raw):
    chk = hashlib.sha256(hashlib.sha256(raw).digest()).digest()[:4]
    return encode(raw + chk)


def decode(data: str) -> bytes:
    """Decode a base58-encoding string, returning bytes"""
    if not data:
        return b''

    # Convert the string to an integer
    n = 0
    for c in data:
        n *= 58
        if c not in base58_alphabet:
            raise ValueError('Character %r is not a valid base58 character' % c)
        digit = base58_alphabet.index(c)
        n += digit

    # Convert the integer to bytes
    h = '%x' % n
    if len(h) % 2:
        h = '0' + h
    res = unhexlify(h.encode('utf8'))

    # Add padding back.
    pad = 0
    for c in data[:-1]:
        if c == base58_alphabet[0]:
            pad += 1
        else:
            break
    return b'\x00' * pad + res


def check_decode(enc):
    dec = decode(enc)
    raw, chk = dec[:-4], dec[-4:]
    if chk != hashlib.sha256(hashlib.sha256(raw).digest()).digest()[:4]:
        raise ValueError("base58 decoding checksum error")
    else:
        return raw
