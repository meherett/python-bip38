#!/usr/bin/env python3

from typing import (
    Union, Literal, Optional
)

import json
import os

from bip38 import BIP38
from bip38.cryptocurrencies import Bitcoin as Cryptocurrency


# Define the passphrase used for encryption/decryption
PASSPHRASE: str = "meherett"
# Pick a random owner salt or use your own
OWNER_SALT: Union[str, bytes] = os.urandom(8)  # Example: "75ed1cdeb254cb38"
# Pick a random seed or use your own
SEED: Union[str, bytes] = os.urandom(24)  # Example: "99241d58245c883896f80843d2846672d7312e6195ca1a6c"
# Specify the WIF type
WIF_TYPE: Literal["wif", "wif-compressed"] = "wif-compressed"
# Define the network type
NETWORK: str = "mainnet"
# Specify the lot number (100000 <= lot <= 999999), or set to None
LOT: Optional[int] = None
# Specify the sequence number (0 <= sequence <= 4095), or set to None
SEQUENCE: Optional[int] = None
# Whether to show detailed information during operations
DETAIL: bool = True

# Initialize the BIP38 object with the cryptocurrency and network
bip38: BIP38 = BIP38(
    cryptocurrency=Cryptocurrency, network=NETWORK
)
# Generate the intermediate passphrase (used in BIP38 encryption)
intermediate_passphrase: str = bip38.intermediate_code(
    passphrase=PASSPHRASE, owner_salt=OWNER_SALT, lot=LOT, sequence=SEQUENCE
)
print("Intermediate Passphrase:", intermediate_passphrase)
# Create a new encrypted WIF (Wallet Import Format) using the intermediate passphrase
encrypted_wif: dict = bip38.create_new_encrypted_wif(
    intermediate_passphrase=intermediate_passphrase, wif_type=WIF_TYPE, seed=SEED
)
print("Encrypted WIF:", json.dumps(encrypted_wif, indent=4))
# Confirm the encrypted WIF using the passphrase and confirmation code
print("Confirm Code:", json.dumps(bip38.confirm_code(
    passphrase=PASSPHRASE, confirmation_code=encrypted_wif["confirmation_code"], detail=DETAIL
), indent=4))
# Decrypt the BIP38 encrypted WIF back to the original private key
print("BIP38 Decrypted:", json.dumps(bip38.decrypt(
    encrypted_wif=encrypted_wif["encrypted_wif"], passphrase=PASSPHRASE, detail=DETAIL
), indent=4))
