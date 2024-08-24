#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import Any
from ecdsa import SigningKey
from ecdsa import (
    curves, keys
)

from ..const import PRIVATE_KEY_LENGTH
from ..exceptions import Secp256k1Error
from .public_key import PublicKey


class PrivateKey:

    signing_key: SigningKey

    def __init__(self, signing_key: SigningKey) -> None:
        """
        Initializes an instance with a signing key.

        :param signing_key: The signing key to be used for cryptographic operations.
        :type signing_key: SigningKey
        """

        self.signing_key = signing_key

    @classmethod
    def from_bytes(cls, private_key: bytes) -> "PrivateKey":
        """
        Creates a private key instance from the given bytes.

        :param private_key: The bytes representing the private key.
        :type private_key: bytes

        :return: An instance of PrivateKey corresponding to the given bytes.
        :rtype: PrivateKey
        """

        try:
            return cls(
                SigningKey.from_string(
                    private_key, curve=curves.SECP256k1
                )
            )
        except keys.MalformedPointError as ex:
            raise Secp256k1Error("Invalid private key bytes") from ex

    @staticmethod
    def length() -> int:
        """
        Returns the length of the private key in bytes for  SECP256k1 curve.

        :return: Length of the private key in bytes.
        :rtype: int
        """

        return PRIVATE_KEY_LENGTH

    def underlying_object(self) -> Any:
        """
        Return the underlying signing key object.

        :return: The underlying signing key object.
        :rtype: Any
        """

        return self.signing_key

    def raw(self) -> bytes:
        """
        Return the raw bytes representation of the private key.

        :return: The raw bytes of the private key.
        :rtype: bytes
        """

        return self.signing_key.to_string()

    def public_key(self) -> PublicKey:
        """
        Retrieve the public key associated with this private key instance.

        :return: The public key object.
        :rtype: IPublicKey
        """

        return PublicKey(self.signing_key.get_verifying_key())
