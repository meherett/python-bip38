#!/usr/bin/env python3

from bip38 import (
    bip38_encrypt, bip38_decrypt
)
from typing import Literal

import json

# Passphrase / password
PASSPHRASE: str = "meherett"
# Wallet Important Format
WIF: str = "938jwjergAxARSWx2YSt9nSBWBz24h8gLhv7EUfgEP1wpMLg6iX"
# Network type
NETWORK: Literal["mainnet", "testnet"] = "testnet"
# To show detail
DETAIL: bool = True

encrypted_wif: str = bip38_encrypt(
    wif=WIF, passphrase=PASSPHRASE, network=NETWORK
)
print("BIP38 Encrypted WIF:", encrypted_wif)

print("BIP38 Decrypted:", json.dumps(bip38_decrypt(
    encrypted_wif=encrypted_wif, passphrase=PASSPHRASE, network=NETWORK, detail=DETAIL
), indent=4))
