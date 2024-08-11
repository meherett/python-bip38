#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from bip38.bip38 import BIP38
from bip38.cryptocurrencies import Bitcoin


def test_intermediate_code(_):

    for index in range(len(_["bip38"]["intermediate_code"])):
        bip38: BIP38 = BIP38(
            cryptocurrency=Bitcoin, network=_["bip38"]["decrypt"][index]["network"]
        )
        intermediate_passphrase: str = bip38.intermediate_code(
            passphrase=_["bip38"]["intermediate_code"][index]["passphrase"],
            lot=_["bip38"]["intermediate_code"][index]["lot"],
            sequence=_["bip38"]["intermediate_code"][index]["sequence"],
            owner_salt=_["bip38"]["intermediate_code"][index]["owner_salt"],
        )

        assert isinstance(intermediate_passphrase, str)

        assert intermediate_passphrase == _["bip38"]["intermediate_code"][index]["intermediate_passphrase"]


def test_bip38_encrypt(_):

    for index in range(len(_["bip38"]["encrypt"])):
        bip38: BIP38 = BIP38(
            cryptocurrency=Bitcoin, network=_["bip38"]["encrypt"][index]["network"]
        )
        encrypted_wif: str = bip38.encrypt(
            wif=_["bip38"]["encrypt"][index]["wif"],
            passphrase=_["bip38"]["encrypt"][index]["passphrase"]
        )

        assert isinstance(encrypted_wif, str)

        assert encrypted_wif == _["bip38"]["encrypt"][index]["encrypted_wif"]


def test_create_new_encrypted_wif(_):

    for index in range(len(_["bip38"]["create_new_encrypted_wif"])):
        bip38: BIP38 = BIP38(
            cryptocurrency=Bitcoin, network="mainnet"
        )
        encrypted_wif: dict = bip38.create_new_encrypted_wif(
            intermediate_passphrase=_["bip38"]["create_new_encrypted_wif"][index]["intermediate_passphrase"],
            public_key_type=_["bip38"]["create_new_encrypted_wif"][index]["public_key_type"],
            seed=_["bip38"]["create_new_encrypted_wif"][index]["seed"]
        )

        assert isinstance(encrypted_wif, dict)

        assert encrypted_wif["encrypted_wif"] == _["bip38"]["create_new_encrypted_wif"][index]["encrypted_wif"]
        assert encrypted_wif["confirmation_code"] == _["bip38"]["create_new_encrypted_wif"][index]["confirmation_code"]
        assert encrypted_wif["public_key"] == _["bip38"]["create_new_encrypted_wif"][index]["public_key"]
        assert encrypted_wif["public_key_type"] == _["bip38"]["create_new_encrypted_wif"][index]["public_key_type"]
        assert encrypted_wif["address"] == _["bip38"]["create_new_encrypted_wif"][index]["address"]


def test_confirm_code(_):

    for index in range(len(_["bip38"]["confirm_code"])):
        bip38: BIP38 = BIP38(
            cryptocurrency=Bitcoin, network="mainnet"
        )
        confirmed: str = bip38.confirm_code(
            passphrase=_["bip38"]["confirm_code"][index]["passphrase"],
            confirmation_code=_["bip38"]["confirm_code"][index]["confirmation_code"],
            detail=False
        )

        assert isinstance(confirmed, str)

        assert confirmed == _["bip38"]["confirm_code"][index]["address"]

        confirmed: dict = bip38.confirm_code(
            passphrase=_["bip38"]["confirm_code"][index]["passphrase"],
            confirmation_code=_["bip38"]["confirm_code"][index]["confirmation_code"],
            detail=True
        )

        assert isinstance(confirmed, dict)

        assert confirmed["public_key"] == _["bip38"]["confirm_code"][index]["public_key"]
        assert confirmed["public_key_type"] == _["bip38"]["confirm_code"][index]["public_key_type"]
        assert confirmed["address"] == _["bip38"]["confirm_code"][index]["address"]
        assert confirmed["lot"] == _["bip38"]["confirm_code"][index]["lot"]
        assert confirmed["sequence"] == _["bip38"]["confirm_code"][index]["sequence"]


def test_bip38_decrypt(_):

    for index in range(len(_["bip38"]["decrypt"])):
        bip38: BIP38 = BIP38(
            cryptocurrency=Bitcoin, network=_["bip38"]["decrypt"][index]["network"]
        )
        decrypted_wif: str = bip38.decrypt(
            encrypted_wif=_["bip38"]["decrypt"][index]["encrypted_wif"],
            passphrase=_["bip38"]["decrypt"][index]["passphrase"],
            detail=False
        )

        assert isinstance(decrypted_wif, str)

        assert decrypted_wif == _["bip38"]["decrypt"][index]["wif"]

        decrypted: dict = bip38.decrypt(
            encrypted_wif=_["bip38"]["decrypt"][index]["encrypted_wif"],
            passphrase=_["bip38"]["decrypt"][index]["passphrase"],
            detail=True
        )

        assert isinstance(decrypted, dict)

        assert decrypted["wif"] == _["bip38"]["decrypt"][index]["wif"]
        assert decrypted["private_key"] == _["bip38"]["decrypt"][index]["private_key"]
        assert decrypted["wif_type"] == _["bip38"]["decrypt"][index]["wif_type"]
        assert decrypted["public_key"] == _["bip38"]["decrypt"][index]["public_key"]
        assert decrypted["public_key_type"] == _["bip38"]["decrypt"][index]["public_key_type"]
        assert decrypted["seed"] == _["bip38"]["decrypt"][index]["seed"]
        assert decrypted["address"] == _["bip38"]["decrypt"][index]["address"]
        assert decrypted["lot"] == _["bip38"]["decrypt"][index]["lot"]
        assert decrypted["sequence"] == _["bip38"]["decrypt"][index]["sequence"]
