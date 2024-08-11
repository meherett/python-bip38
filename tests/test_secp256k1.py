#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ecdsa import (
    SigningKey, VerifyingKey
)
from ecdsa.ellipticcurve import PointJacobi

from bip38.secp256k1 import (
    Secp256k1, Point, PublicKey, PrivateKey
)
from bip38.utils import get_bytes


def test_secp256k1():

    assert isinstance(Secp256k1.ORDER, int)
    assert isinstance(Secp256k1.GENERATOR, Point)
    assert isinstance(Secp256k1.POINT, type(Point))
    assert isinstance(Secp256k1.PUBLIC_KEY, type(PublicKey))
    assert isinstance(Secp256k1.PRIVATE_KEY, type(PrivateKey))


def test_secp256k1_point(_):

    for public_key_type in ["uncompressed", "compressed"]:
        # Test from bytes
        point = Point.from_bytes(
            get_bytes(_["secp256k1"][public_key_type]["point"]["encode"])
        )

        assert isinstance(point, Point)
        assert isinstance(point.underlying_object(), PointJacobi)

        assert point.x() == _["secp256k1"][public_key_type]["point"]["x"]
        assert point.y() == _["secp256k1"][public_key_type]["point"]["y"]
        assert point.raw_encoded() == get_bytes(_["secp256k1"][public_key_type]["point"]["encode"])
        assert point.raw() == point.raw_decoded() == get_bytes(_["secp256k1"][public_key_type]["point"]["decode"])

        # Test from coordinate
        point = Point.from_coordinates(
            x=_["secp256k1"][public_key_type]["point"]["x"],
            y=_["secp256k1"][public_key_type]["point"]["y"]
        )

        assert point.x() == _["secp256k1"][public_key_type]["point"]["x"]
        assert point.y() == _["secp256k1"][public_key_type]["point"]["y"]
        assert point.raw_encoded() == get_bytes(_["secp256k1"][public_key_type]["point"]["encode"])
        assert point.raw() == point.raw_decoded() == get_bytes(_["secp256k1"][public_key_type]["point"]["decode"])


def test_secp256k1_public_key(_):

    assert PublicKey.uncompressed_length() == _["secp256k1"]["uncompressed"]["length"]
    assert PublicKey.compressed_length() == _["secp256k1"]["compressed"]["length"]
    for public_key_type in ["uncompressed", "compressed"]:
        public_key = PublicKey.from_bytes(
            get_bytes(_["secp256k1"][public_key_type]["public_key"])
        )
        assert isinstance(public_key, PublicKey)
        assert isinstance(public_key.point(), Point)
        assert isinstance(public_key.underlying_object(), VerifyingKey)

        assert public_key.raw_uncompressed() == get_bytes(_["secp256k1"]["uncompressed"]["public_key"])
        assert public_key.raw_compressed() == get_bytes(_["secp256k1"]["compressed"]["public_key"])


def test_secp256k1_private_key(_):

    assert PrivateKey.length() == _["secp256k1"]["private_key_length"]
    private_key = PrivateKey.from_bytes(
        get_bytes(_["secp256k1"]["private_key"])
    )

    assert isinstance(private_key, PrivateKey)
    assert isinstance(private_key.underlying_object(), SigningKey)
    assert isinstance(private_key.raw(), bytes)
    assert isinstance(private_key.public_key(), PublicKey)

    assert private_key.raw() == get_bytes(_["secp256k1"]["private_key"])
    assert private_key.public_key().raw_uncompressed() == get_bytes(_["secp256k1"]["uncompressed"]["public_key"])
    assert private_key.public_key().raw_compressed() == get_bytes(_["secp256k1"]["compressed"]["public_key"])
