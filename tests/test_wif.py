#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from bip38.cryptocurrencies import Bitcoin
from bip38.wif import (
    encode_wif, decode_wif
)


def test_wif(_):

    for network in Bitcoin.NETWORKS.keys():

        uncompressed_wif, compressed_wif = encode_wif(
            private_key=_["wif"]["private_key"], wif_prefix=Bitcoin.NETWORKS[network]["wif_prefix"]
        )
        assert _["wif"]["uncompressed"]["wif"][network] == uncompressed_wif
        assert _["wif"]["compressed"]["wif"][network] == compressed_wif

        private_key, wif_type, checksum = decode_wif(
            compressed_wif, wif_prefix=Bitcoin.NETWORKS[network]["wif_prefix"]
        )
        assert private_key.hex() == _["wif"]["private_key"]
        assert wif_type == _["wif"]["compressed"]["wif_type"]
        assert checksum.hex() == _["wif"]["compressed"]["wif_checksum"][network]

        private_key, wif_type, checksum = decode_wif(
            uncompressed_wif, wif_prefix=Bitcoin.NETWORKS[network]["wif_prefix"]
        )
        assert private_key.hex() == _["wif"]["private_key"]
        assert wif_type == _["wif"]["uncompressed"]["wif_type"]
        assert checksum.hex() == _["wif"]["uncompressed"]["wif_checksum"][network]
