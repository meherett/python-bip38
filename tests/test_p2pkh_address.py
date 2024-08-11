#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from bip38.p2pkh_address import P2PKHAddress


def test_p2pkh_address(_):

    assert P2PKHAddress.encode(
        public_key=_["p2pkh_address"]["compressed"]["public_key"],
        public_key_address_prefix=int(_["p2pkh_address"]["compressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["p2pkh_address"]["compressed"]["args"]["public_key_type"]
    ) == _["p2pkh_address"]["compressed"]["encode"]

    assert P2PKHAddress.decode(
        address=_["p2pkh_address"]["compressed"]["encode"],
        public_key_address_prefix=int(_["p2pkh_address"]["compressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["p2pkh_address"]["compressed"]["args"]["public_key_type"]
    ) == _["p2pkh_address"]["compressed"]["decode"]

    assert P2PKHAddress.encode(
        public_key=_["p2pkh_address"]["uncompressed"]["public_key"],
        public_key_address_prefix=int(_["p2pkh_address"]["uncompressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["p2pkh_address"]["uncompressed"]["args"]["public_key_type"]
    ) == _["p2pkh_address"]["uncompressed"]["encode"]

    assert P2PKHAddress.decode(
        address=_["p2pkh_address"]["uncompressed"]["encode"],
        public_key_address_prefix=int(_["p2pkh_address"]["uncompressed"]["args"]["public_key_address_prefix"], base=16),
        public_key_type=_["p2pkh_address"]["uncompressed"]["args"]["public_key_type"]
    ) == _["p2pkh_address"]["uncompressed"]["decode"]
