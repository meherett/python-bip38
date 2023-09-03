#!/usr/bin/env python3

import json
import os

from bip38.utils import (
    get_bytes, bytes_reverse, bytes_to_string, bytes_to_integer, integer_to_bytes, ripemd160, sha256, double_sha256, hash160
)

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_utils():

    assert isinstance(get_bytes(data=_["other"]["private_key"], unhexlify=False), bytes)
    assert isinstance(get_bytes(data=_["other"]["private_key"], unhexlify=True), bytes)
    assert isinstance(bytes_reverse(data=get_bytes(data=_["other"]["private_key"])), bytes)

