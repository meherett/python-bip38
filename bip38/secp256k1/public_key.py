#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Any, Literal
)
from ecdsa import VerifyingKey
from ecdsa.ecdsa import curve_secp256k1
from ecdsa import (
    curves, ellipticcurve, keys
)

from ..const import SECP256K1
from .point import Point


class PublicKey:

    verify_key: VerifyingKey

    def __init__(self, verify_key: VerifyingKey) -> None:
        """
        Initialize the instance with a verifying key.

        :param verify_key: The verifying key used for cryptographic operations.
        :type verify_key: VerifyingKey
        """

        self.verify_key = verify_key

    @classmethod
    def from_bytes(cls, public_key: bytes) -> "PublicKey":
        """
        Create a public key instance from bytes representation.

        :param public_key: The bytes representation of the public key.
        :type public_key: bytes

        :return: An instance of the public key derived from the given bytes.
        :rtype: PublicKey
        """

        try:
            return cls(
                VerifyingKey.from_string(
                    public_key, curve=curves.SECP256k1
                )
            )
        except keys.MalformedPointError as ex:
            raise ValueError("Invalid public key bytes") from ex

    @classmethod
    def from_point(cls, point: Point) -> "PublicKey":
        """
        Create a public key instance from an elliptic curve point.

        :param point: The elliptic curve point representing the public key.
        :type point: Point

        :return: An instance of the public key derived from the given point.
        :rtype: PublicKey
        """

        try:
            return cls(
                VerifyingKey.from_public_point(
                    ellipticcurve.Point(
                        curve_secp256k1, point.x(), point.y()
                    ),
                    curve=curves.SECP256k1
                )
            )
        except keys.MalformedPointError as ex:
            raise ValueError("Invalid public key point") from ex

    @staticmethod
    def compressed_length() -> int:
        """
        Returns the length of a compressed public key in bytes.

        :return: The length of a compressed public key in bytes.
        :rtype: int
        """

        return SECP256K1.PUBLIC_KEY_COMPRESSED_BYTE_LENGTH

    @staticmethod
    def uncompressed_length() -> int:
        """
        Returns the length of an uncompressed public key in bytes.

        :return: The length of an uncompressed public key in bytes.
        :rtype: int
        """

        return SECP256K1.PUBLIC_KEY_UNCOMPRESSED_BYTE_LENGTH

    def underlying_object(self) -> Any:
        """
        Returns the underlying verification key object.

        :return: The underlying verification key object.
        :rtype: Any
        """

        return self.verify_key

    def raw(self, public_key_type: str) -> bytes:
        """
        Retrieves the raw compressed representation of the public key.

        :return: The compressed public key bytes.
        :rtype: bytes
        """

        return self.raw_compressed() if public_key_type == "compressed" else self.raw_uncompressed()

    def raw_compressed(self) -> bytes:
        """
        Retrieves the raw compressed representation of the public key.

        :return: The compressed public key bytes.
        :rtype: bytes
        """

        return self.verify_key.to_string("compressed")

    def raw_uncompressed(self) -> bytes:
        """
        Retrieves the raw uncompressed representation of the public key.

        :return: The uncompressed public key bytes.
        :rtype: bytes
        """

        return self.verify_key.to_string("uncompressed")

    def point(self) -> Point:
        """
        Retrieves the point object associated with the public key.

        :return: The point object implementing the Point interface.
        :rtype: Point
        """

        return Point(self.verify_key.pubkey.point)
