#!/usr/bin/env python3

import hashlib
import six

__base58_alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
__base58_alphabet_bytes = b"123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
__base58_radix = len(__base58_alphabet)


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


def encode(data):
    enc = ""
    val = string_to_int(data)
    while val >= __base58_radix:
        val, mod = divmod(val, __base58_radix)
        enc = __base58_alphabet[mod] + enc
    if val:
        enc = __base58_alphabet[val] + enc

    n = len(data) - len(data.lstrip(b"\0"))
    return __base58_alphabet[0] * n + enc


def check_encode(raw):
    chk = hashlib.sha256(hashlib.sha256(raw).digest()).digest()[:4]
    return encode(raw + chk)


def decode(data):
    if bytes != str:
        data = bytes(data, "ascii")

    val = 0
    prefix = 0
    for c in data:
        val = (val * __base58_radix) + __base58_alphabet_bytes.find(c)
        if val == 0:
            prefix += 1

    dec = bytearray()
    while val > 0:
        val, mod = divmod(val, 256)
        dec.append(mod)

    dec.extend(bytearray(prefix))

    return bytes(dec[::-1])


def check_decode(enc):
    dec = decode(enc)
    raw, chk = dec[:-4], dec[-4:]
    if chk != hashlib.sha256(hashlib.sha256(raw).digest()).digest()[:4]:
        raise ValueError("base58 decoding checksum error")
    else:
        return raw
