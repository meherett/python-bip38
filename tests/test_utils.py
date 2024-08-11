#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

import os

from bip38.utils import (
    get_bytes, bytes_reverse, bytes_to_string, bytes_to_integer, integer_to_bytes
)


def test_utils(_):

    assert isinstance(get_bytes(data=os.urandom(8), unhexlify=False), bytes)
    assert isinstance(get_bytes(data=os.urandom(8), unhexlify=False), bytes)
    assert isinstance(get_bytes(data=bytes_to_string(os.urandom(8)), unhexlify=True), bytes)
    assert isinstance(get_bytes(data=bytes_to_string(os.urandom(8)), unhexlify=True), bytes)
    assert isinstance(bytes_reverse(data=os.urandom(8)), bytes)
    assert isinstance(bytes_to_string(data=str()), str)
    assert isinstance(bytes_to_string(data=os.urandom(8)), str)
    assert isinstance(bytes_to_integer(data=os.urandom(8)), int)
    assert isinstance(integer_to_bytes(bytes_to_integer(data=os.urandom(8))), bytes)
