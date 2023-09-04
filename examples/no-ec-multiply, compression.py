#!/usr/bin/env python3

from bip38 import (
    bip38_encrypt, bip38_decrypt
)

import json

# Passphrase / password
PASSPHRASE: str = "meherett"
# Wallet important format
WIF: str = "L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP"
# To show detail
DETAIL: bool = True

encrypted_wif: str = bip38_encrypt(
    wif=WIF, passphrase=PASSPHRASE
)
print("BIP38 Encrypted WIF:", encrypted_wif)

print("BIP38 Decrypted:", json.dumps(bip38_decrypt(
    encrypted_wif=encrypted_wif, passphrase=PASSPHRASE, detail=DETAIL
), indent=4))
