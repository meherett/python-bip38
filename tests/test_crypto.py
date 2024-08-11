#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit


from bip38.crypto import (
    ripemd160, sha256, double_sha256, get_checksum, hash160
)
from bip38.utils import get_bytes


def test_crypto(_):

    assert isinstance(ripemd160(data=_["crypto"]["data"]), bytes)
    assert ripemd160(data=_["crypto"]["data"]) == get_bytes(_["crypto"]["ripemd160"])

    assert isinstance(sha256(data=_["crypto"]["data"]), bytes)
    assert sha256(data=_["crypto"]["data"]) == get_bytes(_["crypto"]["sha256"])

    assert isinstance(double_sha256(data=_["crypto"]["data"]), bytes)
    assert double_sha256(data=_["crypto"]["data"]) == get_bytes(_["crypto"]["double_sha256"])

    assert isinstance(get_checksum(data=_["crypto"]["data"]), bytes)
    assert get_checksum(data=_["crypto"]["data"]) == get_bytes(_["crypto"]["get_checksum"])

    assert isinstance(hash160(data=_["crypto"]["data"]), bytes)
    assert hash160(data=_["crypto"]["data"]) == get_bytes(_["crypto"]["hash160"])
