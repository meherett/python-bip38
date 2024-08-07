#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ecdsa.ecdsa import generator_secp256k1

from .point import Point
from .public_key import PublicKey
from .private_key import PrivateKey


class Secp256k1:  # Elliptic Curve Cryptography (ECC)

    ORDER: str = generator_secp256k1.order()
    GENERATOR = Point(generator_secp256k1)
    POINT = Point
    PUBLIC_KEY = PublicKey
    PRIVATE_KEY = PrivateKey
