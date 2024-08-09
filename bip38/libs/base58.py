#!/usr/bin/env python3

from hashlib import sha256

import six

__base58_alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


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


def encode(data, alphabet=__base58_alphabet):
    enc = ""
    val = string_to_int(data)
    while val >= len(alphabet):
        val, mod = divmod(val, len(alphabet))
        enc = alphabet[mod] + enc
    if val:
        enc = alphabet[val] + enc

    n = len(data) - len(data.lstrip(b"\0"))
    return alphabet[0] * n + enc


def check_encode(raw, alphabet=__base58_alphabet):
    chk = sha256(sha256(raw).digest()).digest()[:4]
    return encode(raw + chk, alphabet)


def decode(data, alphabet=__base58_alphabet):
    if bytes != str:
        data = bytes(data, "ascii")

    val = 0
    prefix = 0
    for c in data:
        val = (val * len(alphabet)) + alphabet.encode("utf-8").find(c)
        if val == 0:
            prefix += 1

    dec = bytearray()
    while val > 0:
        val, mod = divmod(val, 256)
        dec.append(mod)

    dec.extend(bytearray(prefix))

    return bytes(dec[::-1])


def check_decode(enc, alphabet=__base58_alphabet):
    dec = decode(enc, alphabet)
    raw, chk = dec[:-4], dec[-4:]
    if chk != sha256(sha256(raw).digest()).digest()[:4]:
        raise ValueError("base58 decoding checksum error")
    else:
        return raw
