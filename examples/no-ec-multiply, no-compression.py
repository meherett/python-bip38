#!/usr/bin/env python3

import json

from bip38 import BIP38
from bip38.cryptocurrencies import Bitcoin as Cryptocurrency

# Define the passphrase used for encryption/decryption
PASSPHRASE: str = "meherett"
# Specify the Wallet Import Format (WIF)
WIF: str = "5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR"  # wif type
# Define the network type
NETWORK: str = "mainnet"
# Whether to show detailed information during operations
DETAIL: bool = True

# Initialize the BIP38 object with the cryptocurrency and network
bip38: BIP38 = BIP38(
    cryptocurrency=Cryptocurrency, network=NETWORK
)
# Encrypt the WIF using the BIP38 standard and the specified passphrase
encrypted_wif: str = bip38.encrypt(
    wif=WIF, passphrase=PASSPHRASE
)
print("BIP38 Encrypted WIF:", encrypted_wif)
# Decrypt the BIP38 encrypted WIF back to the original private key and show details
print("BIP38 Decrypted:", json.dumps(bip38.decrypt(
    encrypted_wif=encrypted_wif, passphrase=PASSPHRASE, detail=DETAIL
), indent=4))
