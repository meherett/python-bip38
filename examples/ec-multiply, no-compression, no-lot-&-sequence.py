#!/usr/bin/env python3

from bip38 import (
    intermediate_code, create_new_encrypted_wif, confirm_code, bip38_decrypt
)
from typing import (
    Union, Optional, Literal
)

import json
import os

# Passphrase / password
PASSPHRASE: str = "meherett"  # "TestingOneTwoThree", "Satoshi" or u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
# Pick random owner salt / use your own salt
OWNER_SALT: Union[str, bytes] = os.urandom(8)  # "75ed1cdeb254cb38"
# Pick random seed / use your own seed
SEED: Union[str, bytes] = os.urandom(24)  # "99241d58245c883896f80843d2846672d7312e6195ca1a6c"
# Public key type
PUBLIC_KEY_TYPEs: list = ["uncompressed", "compressed"]
# Network type
NETWORK: Literal["mainnet", "testnet"] = "testnet"
# 100000 <= lot <= 999999 / set none
LOT: Optional[int] = None
# 0 <= sequence <= 4095 / set none
SEQUENCE: Optional[int] = None
# To show detail
DETAIL: bool = True

intermediate_passphrase: str = intermediate_code(
    passphrase=PASSPHRASE, owner_salt=OWNER_SALT, lot=LOT, sequence=SEQUENCE
)

print("Intermediate Passphrase:", intermediate_passphrase)

for PUBLIC_KEY_TYPE in PUBLIC_KEY_TYPEs:
    encrypted_wif: dict = create_new_encrypted_wif(
        intermediate_passphrase=intermediate_passphrase, public_key_type=PUBLIC_KEY_TYPE, seed=SEED, network=NETWORK
    )
    print("Encrypted WIF:", json.dumps(encrypted_wif, indent=4))

    print("Confirm Code:", json.dumps(confirm_code(
        passphrase=PASSPHRASE, confirmation_code=encrypted_wif["confirmation_code"], network=NETWORK, detail=DETAIL
    ), indent=4))

    print("BIP38 Decrypted:", json.dumps(bip38_decrypt(
        encrypted_wif=encrypted_wif["encrypted_wif"], passphrase=PASSPHRASE, network=NETWORK, detail=DETAIL
    ), indent=4))
