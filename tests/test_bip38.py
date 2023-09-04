#!/usr/bin/env python3

import json
import os

from bip38.bip38 import (
    bip38_encrypt, bip38_decrypt, intermediate_code, create_new_encrypted_wif, confirm_code,
    # Importing other functions for testing
    private_key_to_public_key, public_key_to_addresses, private_key_to_wif,
    get_wif_type, wif_to_private_key, get_wif_checksum
)

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_bip38_encrypt():

    for index in range(len(_["bip38"]["bip38_encrypt"])):

        encrypted_wif: str = bip38_encrypt(
            wif=_["bip38"]["bip38_encrypt"][index]["wif"],
            passphrase=_["bip38"]["bip38_encrypt"][index]["passphrase"],
        )

        assert isinstance(encrypted_wif, str)

        assert encrypted_wif == _["bip38"]["bip38_encrypt"][index]["encrypted_wif"]


def test_bip38_decrypt():

    for index in range(len(_["bip38"]["bip38_decrypt"])):

        decrypted_wif: str = bip38_decrypt(
            encrypted_wif=_["bip38"]["bip38_decrypt"][index]["encrypted_wif"],
            passphrase=_["bip38"]["bip38_decrypt"][index]["passphrase"],
            detail=False
        )

        assert isinstance(decrypted_wif, str)

        assert decrypted_wif == _["bip38"]["bip38_decrypt"][index]["wif"]

        decrypted: dict = bip38_decrypt(
            encrypted_wif=_["bip38"]["bip38_decrypt"][index]["encrypted_wif"],
            passphrase=_["bip38"]["bip38_decrypt"][index]["passphrase"],
            detail=True
        )

        assert isinstance(decrypted, dict)

        assert decrypted["wif"] == _["bip38"]["bip38_decrypt"][index]["wif"]
        assert decrypted["private_key"] == _["bip38"]["bip38_decrypt"][index]["private_key"]
        assert decrypted["wif_type"] == _["bip38"]["bip38_decrypt"][index]["wif_type"]
        assert decrypted["public_key"] == _["bip38"]["bip38_decrypt"][index]["public_key"]
        assert decrypted["public_key_type"] == _["bip38"]["bip38_decrypt"][index]["public_key_type"]
        assert decrypted["seed"] == _["bip38"]["bip38_decrypt"][index]["seed"]
        assert decrypted["address"] == _["bip38"]["bip38_decrypt"][index]["address"]
        assert decrypted["lot"] == _["bip38"]["bip38_decrypt"][index]["lot"]
        assert decrypted["sequence"] == _["bip38"]["bip38_decrypt"][index]["sequence"]


def test_intermediate_code():

    for index in range(len(_["bip38"]["intermediate_code"])):

        intermediate_passphrase: str = intermediate_code(
            passphrase=_["bip38"]["intermediate_code"][index]["passphrase"],
            lot=_["bip38"]["intermediate_code"][index]["lot"],
            sequence=_["bip38"]["intermediate_code"][index]["sequence"],
            owner_salt=_["bip38"]["intermediate_code"][index]["owner_salt"],
        )

        assert isinstance(intermediate_passphrase, str)

        assert intermediate_passphrase == _["bip38"]["intermediate_code"][index]["intermediate_passphrase"]


def test_create_new_encrypted_wif():

    for index in range(len(_["bip38"]["create_new_encrypted_wif"])):

        encrypted_wif: dict = create_new_encrypted_wif(
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


def test_confirm_code():

    for index in range(len(_["bip38"]["confirm_code"])):

        confirmed: str = confirm_code(
            passphrase=_["bip38"]["confirm_code"][index]["passphrase"],
            confirmation_code=_["bip38"]["confirm_code"][index]["confirmation_code"],
            detail=False
        )

        assert isinstance(confirmed, str)

        assert confirmed == _["bip38"]["confirm_code"][index]["address"]

        confirmed: dict = confirm_code(
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


def test_other_functions():

    assert private_key_to_wif(
        private_key=_["other"]["private_key"], wif_type=_["other"]["uncompressed"]["wif_type"]
    ) == _["other"]["uncompressed"]["wif"]

    assert private_key_to_wif(
        private_key=_["other"]["private_key"], wif_type=_["other"]["compressed"]["wif_type"]
    ) == _["other"]["compressed"]["wif"]

    assert private_key_to_public_key(
        private_key=_["other"]["private_key"], public_key_type=_["other"]["uncompressed"]["public_key_type"]
    ) == _["other"]["uncompressed"]["public_key"]

    assert private_key_to_public_key(
        private_key=_["other"]["private_key"], public_key_type=_["other"]["compressed"]["public_key_type"]
    ) == _["other"]["compressed"]["public_key"]

    assert public_key_to_addresses(
        public_key=_["other"]["uncompressed"]["public_key"]
    ) == _["other"]["uncompressed"]["address"]

    assert public_key_to_addresses(
        public_key=_["other"]["compressed"]["public_key"]
    ) == _["other"]["compressed"]["address"]

    assert get_wif_type(wif=_["other"]["uncompressed"]["wif"]) == _["other"]["uncompressed"]["wif_type"]

    assert get_wif_type(wif=_["other"]["compressed"]["wif"]) == _["other"]["compressed"]["wif_type"]

    assert wif_to_private_key(wif=_["other"]["uncompressed"]["wif"]) == _["other"]["private_key"]

    assert wif_to_private_key(wif=_["other"]["compressed"]["wif"]) == _["other"]["private_key"]

    assert get_wif_checksum(wif=_["other"]["uncompressed"]["wif"]) == _["other"]["uncompressed"]["wif_checksum"]

    assert get_wif_checksum(wif=_["other"]["compressed"]["wif"]) == _["other"]["compressed"]["wif_checksum"]
