#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Any, Union
)

from bip38.libs.base58 import (
    ensure_string, check_encode, check_decode
)
from bip38.const import PUBLIC_KEY_TYPES
from bip38.secp256k1 import PublicKey
from bip38.prefixes import PREFIXES

from bip38.utils import (
    integer_to_bytes, bytes_to_string, hash160, get_bytes
)


class P2PKHAddress:
    
    address_prefix: int = PREFIXES["Bitcoin"]["NETWORKS"]["MAINNET"]["ADDRESS_PREFIX"]
    alphabet: str = PREFIXES["Bitcoin"]["ALPHABET"]

    @classmethod
    def encode(cls, public_key: Union[bytes, str, PublicKey], **kwargs: Any) -> str:
        """
        Encode a public key into an address using a specified address prefix and alphabet.

        :param public_key: The public key to encode.
        :type public_key: Union[bytes, str, IPublicKey]
        :param kwargs: Additional keyword arguments.
            - address_prefix: Address prefix for the public key (optional).
            - public_key_type: Type of the public key (optional).
            - alphabet: Custom alphabet for encoding (optional).
        :type kwargs: Any

        :return: The encoded address.
        :rtype: str
        """

        address_prefix: bytes = integer_to_bytes(
            kwargs.get("address_prefix", cls.address_prefix)
        )

        if not isinstance(public_key, PublicKey):
            public_key: PublicKey = PublicKey.from_bytes(get_bytes(public_key))

        public_key_hash: bytes = hash160(
            public_key.raw_compressed()
            if kwargs.get("public_key_type", PUBLIC_KEY_TYPES.COMPRESSED) == PUBLIC_KEY_TYPES.COMPRESSED else
            public_key.raw_uncompressed()
        )

        return ensure_string(check_encode(
            (address_prefix + public_key_hash), alphabet=kwargs.get(
                "alphabet", cls.alphabet
            )
        ))

    @classmethod
    def decode(cls, address: str, **kwargs: Any) -> str:
        """
        Decode an address string into a public key hash using a specified address prefix and alphabet.

        :param address: The address string to decode.
        :type address: str
        :param kwargs: Additional keyword arguments.
            - address_prefix: Address prefix for the public key (optional).
            - alphabet: Custom alphabet for decoding (optional).
        :type kwargs: Any

        :return: The decoded public key hash as a string.
        :rtype: str
        """

        address_prefix: bytes = integer_to_bytes(
            kwargs.get("address_prefix", cls.address_prefix)
        )
        address_decode: bytes = check_decode(
            address, alphabet=kwargs.get(
                "alphabet", cls.alphabet
            )
        )

        expected_length: int = 20 + len(address_prefix)
        if len(address_decode) != expected_length:
            raise ValueError(f"Invalid length (expected: {expected_length}, got: {len(address_decode)})")

        prefix_got: bytes = address_decode[:len(address_prefix)]
        if address_prefix != prefix_got:
            raise ValueError(f"Invalid prefix (expected: {address_prefix}, got: {prefix_got})")

        return bytes_to_string(address_decode[len(address_prefix):])
