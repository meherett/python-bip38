<h1 align="center" style="border-bottom: none">
    <img height="100" alt="BIP38" src="docs/static/svg/bip38.svg"><br>Bitcoin Improvement Proposal - 0038
</h1>

<p align="center">
    <a href="https://github.com/meherett/python-bip38/releases" target="_blank">Releases</a> · <a href="https://talonlab.gitbook.io/bip38/manual" target="_blank">Manual</a> · <a href="https://bip38.readthedocs.io" target="_blank">API Docs</a> · <a href="#donations">Donation</a>
</p>

<div align="center">

[![Build Status](https://img.shields.io/github/actions/workflow/status/meherett/python-bip38/build.yml)](https://github.com/meherett/python-bip38/actions/workflows/build.yml)
[![PyPI Version](https://img.shields.io/pypi/v/bip38.svg?color=blue)](https://pypi.org/project/bip38)
[![Documentation Status](https://readthedocs.org/projects/bip38/badge/?version=master)](https://bip38.readthedocs.io)
[![PyPI License](https://img.shields.io/pypi/l/bip38?color=black)](https://pypi.org/project/bip38)
[![PyPI Python Version](https://img.shields.io/pypi/pyversions/bip38.svg)](https://pypi.org/project/bip38)
[![Coverage Status](https://coveralls.io/repos/github/meherett/python-bip38/badge.svg?branch=master)](https://coveralls.io/github/meherett/python-bip38)

</div>

A Python library for the implementation of Bitcoin Improvement Proposal - 0038 / (BIP38) protocol.
This library supports both [No EC-multiply](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki#encryption-when-ec-multiply-flag-is-not-used) and [EC-multiply](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki#encryption-when-ec-multiply-mode-is-used) modes and is compatible with over 150+ cryptocurrencies.
It's specifically tailored for Pay-to-PubKey-Hash (P2PKH) address types.

![Desktop Application](docs/static/gif/bip38.gif)

For more info see the [Passphrase-protected private key - BIP38](https://en.bitcoin.it/wiki/BIP_0038) spec.

## Installation

The easiest way to install `bip38` is via pip:

```
pip install bip38
```

If you want to run the latest version of the code, you can install from the git:

```
pip install git+git://github.com/meherett/python-bip38.git
```

## Quick Usage

##### no EC multiply:

```python
#!/usr/bin/env python3

from typing import List

import json

from bip38 import BIP38
from bip38.cryptocurrencies import Bitcoin as Cryptocurrency
from bip38.wif import private_key_to_wif

# Private key
PRIVATE_KEY: str = "cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5"
# Passphrase / password
PASSPHRASE: str = "meherett"  # u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
# Network type
NETWORK:str = "mainnet"
# To show detail
DETAIL: bool = True
# Initialize BIP38 instance
bip38: BIP38 = BIP38(
    cryptocurrency=Cryptocurrency, network=NETWORK
)
# Wallet Import Format's
WIFs: List[str] = [
    private_key_to_wif(
        private_key=PRIVATE_KEY, cryptocurrency=Cryptocurrency, network=NETWORK, wif_type="wif"
    ),  # No compression
    private_key_to_wif(
        private_key=PRIVATE_KEY, cryptocurrency=Cryptocurrency, network=NETWORK, wif_type="wif-compressed"
    )  # Compression
]

for WIF in WIFs:
    
    print("WIF:", WIF)

    encrypted_wif: str = bip38.encrypt(
        wif=WIF, passphrase=PASSPHRASE
    )
    print("BIP38 Encrypted WIF:", encrypted_wif)
    
    print("BIP38 Decrypted:", json.dumps(bip38.decrypt(
        encrypted_wif=encrypted_wif, passphrase=PASSPHRASE, detail=DETAIL
    ), indent=4))

    print("-" * 125)
```

<details open>
  <summary>Output</summary><br/>

```shell
WFI: 5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR
BIP38 Encrypted WIF: 6PRVWUbkzNehVoPSCKYviigdnwsck69PLiMPpTVWGENzUAy7spnAZqnxit
BIP38 Decrypted: {
    "wif": "5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR",
    "private_key": "cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5",
    "wif_type": "wif",
    "public_key": "04d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360ea7f23327b49ba7f10d17fad15f068b8807dbbc9e4ace5d4a0b40264eefaf31a4",
    "public_key_type": "uncompressed",
    "seed": null,
    "address": "1Jq6MksXQVWzrznvZzxkV6oY57oWXD9TXB",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
WFI: L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP
BIP38 Encrypted WIF: 6PYNKZ1EASfdDgcUgtxxRi7DkYPTXzwYUzEqzDxv2H8QbeKDV9D9wBWUA7
BIP38 Decrypted: {
    "wif": "L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP",
    "private_key": "cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5",
    "wif_type": "wif-compressed",
    "public_key": "02d2ce831dd06e5c1f5b1121ef34c2af4bcb01b126e309234adbc3561b60c9360e",
    "public_key_type": "compressed",
    "seed": null,
    "address": "164MQi977u9GUteHr4EPH27VkkdxmfCvGW",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
```
</details>

##### EC multiply:

```python
#!/usr/bin/env python3

from typing import List

import json
import os

from bip38 import BIP38
from bip38.cryptocurrencies import Bitcoin as Cryptocurrency

# Passphrase / password
PASSPHRASE: str = "meherett"  # u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
# Network type
NETWORK: str = "mainnet"
# To show detail
DETAIL: bool = True
# Initialize BIP38 instance
bip38: BIP38 = BIP38(
    cryptocurrency=Cryptocurrency, network=NETWORK
)
# List of owner salt, seed, public key type, lot, and sequence kwargs
KWARGS: List[dict] = [
    # Random owner salt & seed, No compression, No lot & sequence
    {"owner_salt": os.urandom(8), "seed": os.urandom(24), "wif_type": "wif", "lot": None, "sequence": None},
    # Random owner salt & seed, No compression, With lot & sequence
    {"owner_salt": os.urandom(8), "seed": os.urandom(24), "wif_type": "wif", "lot": 863741, "sequence": 1},
    # Random owner salt & seed, Compression, No lot & sequence
    {"owner_salt": os.urandom(8), "seed": os.urandom(24), "wif_type": "wif-compressed", "lot": None, "sequence": None},
    # Random owner salt & seed, Compression, With lot & sequence
    {"owner_salt": os.urandom(8), "seed": os.urandom(24), "wif_type": "wif-compressed", "lot": 863741, "sequence": 1},
    # With owner salt & seed, No compression, No lot & sequence
    {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "wif_type": "wif", "lot": None, "sequence": None},
    # With owner salt & seed, No compression, With lot & sequence
    {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "wif_type": "wif", "lot": 567885, "sequence": 1},
    # With owner salt & seed, Compression, No lot & sequence
    {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "wif_type": "wif-compressed", "lot": None, "sequence": None},
    # With owner salt & seed, Compression, With lot & sequence
    {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "wif_type": "wif-compressed", "lot": 369861, "sequence": 1},
]

for kwarg in KWARGS:
    
    intermediate_passphrase: str = bip38.intermediate_code(
        passphrase=PASSPHRASE, owner_salt=kwarg["owner_salt"], lot=kwarg["lot"], sequence=kwarg["sequence"]
    )
    print("Intermediate Passphrase:", intermediate_passphrase)

    encrypted_wif: dict = bip38.create_new_encrypted_wif(
        intermediate_passphrase=intermediate_passphrase, wif_type=kwarg["wif_type"], seed=kwarg["seed"],
    )
    print("Encrypted WIF:", json.dumps(encrypted_wif, indent=4))

    print("Confirm Code:", json.dumps(bip38.confirm_code(
        passphrase=PASSPHRASE, confirmation_code=encrypted_wif["confirmation_code"], detail=DETAIL
    ), indent=4))

    print("BIP38 Decrypted:", json.dumps(bip38.decrypt(
        encrypted_wif=encrypted_wif["encrypted_wif"], passphrase=PASSPHRASE, detail=DETAIL
    ), indent=4))

    print("-" * 125)
```

<details>
  <summary>Output</summary><br/>

```shell
Intermediate Passphrase: passphrasemPCQA1bnn4UUz4fKQyGxxmRh3aXjTQnFcqzHreFSkcpCRatZwwpphgbscdDCZu
Encrypted WIF: {
    "encrypted_wif": "6PfWfN5oVWW7L4FwCfWNzwyjqRjV4N8VfYKmhW3FBKQ3Ye622bb5UuAHPS",
    "confirmation_code": "cfrm38V5oAdNKq1FqxhoKmAdf1gNYxS2HKBwqS2W1D4zmgfpv8AZeLXJXbvTEkZoDaJ9TKKaMne",
    "public_key": "0461b5e4a6fbfb6fda76a56cda81a8212c40a5dd7ae7a6ad4f949eb6754c78cc3586a8ccff2b3804d6c8b30cdf66a943466f61470f3e16421eeabea77af60c323c",
    "seed": "ebda4e39aecc735594ebcdc09884eba498df3c029a18fc87",
    "public_key_type": "uncompressed",
    "address": "1Pyq2x2rAHLcwBohNRePsEDkF7W3S2n4Y8"
}
Confirm Code: {
    "public_key": "0461b5e4a6fbfb6fda76a56cda81a8212c40a5dd7ae7a6ad4f949eb6754c78cc3586a8ccff2b3804d6c8b30cdf66a943466f61470f3e16421eeabea77af60c323c",
    "public_key_type": "uncompressed",
    "address": "1Pyq2x2rAHLcwBohNRePsEDkF7W3S2n4Y8",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "5K4EF2MxNbvSc6Yhgv3oFDRRdjQjvMWE4x28BzeaW3RvxN6FkyU",
    "private_key": "a35aa5ea84d0896c62bc3c4456a224800970d37f6f89ecc0bc27e52a114977e6",
    "wif_type": "wif",
    "public_key": "0461b5e4a6fbfb6fda76a56cda81a8212c40a5dd7ae7a6ad4f949eb6754c78cc3586a8ccff2b3804d6c8b30cdf66a943466f61470f3e16421eeabea77af60c323c",
    "public_key_type": "uncompressed",
    "seed": "ebda4e39aecc735594ebcdc09884eba498df3c029a18fc87",
    "address": "1Pyq2x2rAHLcwBohNRePsEDkF7W3S2n4Y8",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseYhgPNmgeMKW83mQbXW54e4mkkUnd2VRHmNdEq5p3RqRxycziF4f6SLdo4vhZGo
Encrypted WIF: {
    "encrypted_wif": "6PgLWy958ySQGGGiK3SWPBfmhMdWndzuSiDMfBQiskmfzQjjJ7EA3LR1tQ",
    "confirmation_code": "cfrm38V8V74UD2Ef4EmEqgAyiHFny8W8h99PjjHwabUcuFA24A56BFmHAB8T46H1XBsWidaBdQL",
    "public_key": "04266c15371b6f3331d0f5f6487153a0ec3e50efeb112470fc43aa6ff2915b9f48b6676629fa1eba9fbb26d6d601e7041f8ef6cc3a6a0cbcfb668074a203aa7036",
    "seed": "bfd386d285386b43f7e7cf467bb06cd4926f0b3d322fd578",
    "public_key_type": "uncompressed",
    "address": "1Q1MUMMEbGczofkLiXZZbGcZNGnFBb3zM8"
}
Confirm Code: {
    "public_key": "04266c15371b6f3331d0f5f6487153a0ec3e50efeb112470fc43aa6ff2915b9f48b6676629fa1eba9fbb26d6d601e7041f8ef6cc3a6a0cbcfb668074a203aa7036",
    "public_key_type": "uncompressed",
    "address": "1Q1MUMMEbGczofkLiXZZbGcZNGnFBb3zM8",
    "lot": 863741,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "5K1X75CJR4vEBh3dGek94c4wta9f4PcGnXzSusP6fcBBrSivS2K",
    "private_key": "9d33cfac10985552c46f4bef6e0a1b3be6934f89505f2c72fb369b9a707d002b",
    "wif_type": "wif",
    "public_key": "04266c15371b6f3331d0f5f6487153a0ec3e50efeb112470fc43aa6ff2915b9f48b6676629fa1eba9fbb26d6d601e7041f8ef6cc3a6a0cbcfb668074a203aa7036",
    "public_key_type": "uncompressed",
    "seed": "bfd386d285386b43f7e7cf467bb06cd4926f0b3d322fd578",
    "address": "1Q1MUMMEbGczofkLiXZZbGcZNGnFBb3zM8",
    "lot": 863741,
    "sequence": 1
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphrasemJ3X3pNLKLC8crc2obQGDP8SbNSdRdLJq2gDAX5u7Lz4boYRRePo1poeHki7Fz
Encrypted WIF: {
    "encrypted_wif": "6PnQA3hpiizx1AtX1gfx4CfmyxWNm8pnDN31efWntycsVhfLU6v6LYzCtQ",
    "confirmation_code": "cfrm38VUEwMBdVAiTWS6VbAgHcLa7HMofzDcL4RsAfLpgPabqa5HcAApGV2YDJnmuFbcFjQ97ZC",
    "public_key": "036dc1541e29df17ee74b483dd8fe5cadd88da1b3f1b24c1bbfcb7595aca3e1b67",
    "seed": "975730a1a70bcc1681f28a53daa90164a67d1cba800b086f",
    "public_key_type": "compressed",
    "address": "14fLQxFW9PdvvrueWJKBcoCSKSEcUBFsVG"
}
Confirm Code: {
    "public_key": "036dc1541e29df17ee74b483dd8fe5cadd88da1b3f1b24c1bbfcb7595aca3e1b67",
    "public_key_type": "compressed",
    "address": "14fLQxFW9PdvvrueWJKBcoCSKSEcUBFsVG",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "L4TUrZr1NYbhrrkky6FQ7dsQSaGJv9GQQ4adPHysftByGWGwbCnR",
    "private_key": "d7f21834c5deea162b6bd6fdb22c7155aea4d7467d8c3caa3f38e1873da3557c",
    "wif_type": "wif-compressed",
    "public_key": "036dc1541e29df17ee74b483dd8fe5cadd88da1b3f1b24c1bbfcb7595aca3e1b67",
    "public_key_type": "compressed",
    "seed": "975730a1a70bcc1681f28a53daa90164a67d1cba800b086f",
    "address": "14fLQxFW9PdvvrueWJKBcoCSKSEcUBFsVG",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseazADit3HysrPUxPQ5AT6uVku3baWtNnNvEhSLu8j7HsAfi1yXc2i8grdQ6c69m
Encrypted WIF: {
    "encrypted_wif": "6PoJKygGkurVG7M5irdCZRw6uQ5g41SuJBsdxGnz7c3345cW8e5FRLU6oj",
    "confirmation_code": "cfrm38VXAwUqLBKTncF2N3KQ8P7moHbEG8161X2XuNEi3H5hYQLZGeBUQKDFH36R9bTNAb1Nvt8",
    "public_key": "0236efe6b2424ae586285c54fa85975253def57a346171f8099d05f1141d44c8b4",
    "seed": "ca1799e4c398ec6c2e76d070977a38a7831db1c48bf3299a",
    "public_key_type": "compressed",
    "address": "15CBXmKhqjZsozC34qwogKAcTVzAfx7ExZ"
}
Confirm Code: {
    "public_key": "0236efe6b2424ae586285c54fa85975253def57a346171f8099d05f1141d44c8b4",
    "public_key_type": "compressed",
    "address": "15CBXmKhqjZsozC34qwogKAcTVzAfx7ExZ",
    "lot": 863741,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "L22EnKuUvu2dSdbS2gV3VzMVYPzCsfo8z7VyMwKDhsTpjcSCYhB3",
    "private_key": "8f48fd8acbe206d77fafa605fdc7356296074b543e43048123873dd9db7d1174",
    "wif_type": "wif-compressed",
    "public_key": "0236efe6b2424ae586285c54fa85975253def57a346171f8099d05f1141d44c8b4",
    "public_key_type": "compressed",
    "seed": "ca1799e4c398ec6c2e76d070977a38a7831db1c48bf3299a",
    "address": "15CBXmKhqjZsozC34qwogKAcTVzAfx7ExZ",
    "lot": 863741,
    "sequence": 1
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseondJwvQGEWFNrNJRPi4G5XAL5SU777GwTNtqmDXqA3CGP7HXfH6AdBxxc5WUKC
Encrypted WIF: {
    "encrypted_wif": "6PfP7T3iQ5jLJLsH5DneySLLF5bhd879DHW87Pxzwtwvn2ggcncxsNKN5c",
    "confirmation_code": "cfrm38V5NZfTZKRaRDTvFAMkNKqKAxTxdDjDdb5RpFfXrVRw7Nov5m2iP3K1Eg5QQRxs52kgapy",
    "public_key": "04cdcd8f846a73e75c8a845d1df19dc23031648c219d1efc6fe945cd089f3052b09e25cb1d8628cd559c6c57c627fa486b8d452da89c1e9778ea967822188990a4",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "uncompressed",
    "address": "18VLTHgu95JPi1iLRtN2WwYroAHvHwE2Ws"
}
Confirm Code: {
    "public_key": "04cdcd8f846a73e75c8a845d1df19dc23031648c219d1efc6fe945cd089f3052b09e25cb1d8628cd559c6c57c627fa486b8d452da89c1e9778ea967822188990a4",
    "public_key_type": "uncompressed",
    "address": "18VLTHgu95JPi1iLRtN2WwYroAHvHwE2Ws",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "5Jh21edvnWUXFjRz8mDVN3CSPp1CyTuUSFBKZeWYU726R6MW3ux",
    "private_key": "733134eb516f94aa56ab7ef0874a0d71daf38c5c009dec2a1261861a15889631",
    "wif_type": "wif",
    "public_key": "04cdcd8f846a73e75c8a845d1df19dc23031648c219d1efc6fe945cd089f3052b09e25cb1d8628cd559c6c57c627fa486b8d452da89c1e9778ea967822188990a4",
    "public_key_type": "uncompressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "18VLTHgu95JPi1iLRtN2WwYroAHvHwE2Ws",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseb7ruSNPsLdQF7t1gh7fs1xvWB4MKDssFQwL11EHkVr4njFX5PtsCUqQqwzh9rS
Encrypted WIF: {
    "encrypted_wif": "6PgKxJUke6BcDc1XuvPDKCD9krZEebapef98SJ3YAjWQHtR3EVsaeK62ja",
    "confirmation_code": "cfrm38V8TGcdd9WSGpaB56JaiW7cbvv1ZD89BHjBGu7S7yUFGcht8CqFQoexCHCoiCp4JzsH1Pk",
    "public_key": "049afcaa528358eddf54634fee9505e90b9572f8733b94260c94d20b563a65a1c94c338d5c09d20c5895d89bd5a2ba39f96ae4b1cf637828714c432042172723b6",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "uncompressed",
    "address": "1DkQJuST62GkJP9kss68fHT8ftLf4SmLVT"
}
Confirm Code: {
    "public_key": "049afcaa528358eddf54634fee9505e90b9572f8733b94260c94d20b563a65a1c94c338d5c09d20c5895d89bd5a2ba39f96ae4b1cf637828714c432042172723b6",
    "public_key_type": "uncompressed",
    "address": "1DkQJuST62GkJP9kss68fHT8ftLf4SmLVT",
    "lot": 567885,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "5JGYLxWwyh9agrM6u63RadubRFjTxbDtvBcQ5EywZrHXBLpPrZW",
    "private_key": "3b9d38cb7d1d97efad80b3934cb1928ae70179317ea4657aaffcdff029f43b90",
    "wif_type": "wif",
    "public_key": "049afcaa528358eddf54634fee9505e90b9572f8733b94260c94d20b563a65a1c94c338d5c09d20c5895d89bd5a2ba39f96ae4b1cf637828714c432042172723b6",
    "public_key_type": "uncompressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "1DkQJuST62GkJP9kss68fHT8ftLf4SmLVT",
    "lot": 567885,
    "sequence": 1
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseondJwvQGEWFNrNJRPi4G5XAL5SU777GwTNtqmDXqA3CGP7HXfH6AdBxxc5WUKC
Encrypted WIF: {
    "encrypted_wif": "6PnUVPinrvPGwoYJK3GbGBNgFuqEXmfvagE4QiAxj7yrZp4i29p22MrY5r",
    "confirmation_code": "cfrm38VUV4NK45caNN5aomS3dSQLT3FVHq556kehuZX1RNuPs8ArWjw18KCCjyTXktVCDBW65pZ",
    "public_key": "02cdcd8f846a73e75c8a845d1df19dc23031648c219d1efc6fe945cd089f3052b0",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "compressed",
    "address": "1BPmkfRYzPAkeErMS6DLDYxPvQEEkoVRz1"
}
Confirm Code: {
    "public_key": "02cdcd8f846a73e75c8a845d1df19dc23031648c219d1efc6fe945cd089f3052b0",
    "public_key_type": "compressed",
    "address": "1BPmkfRYzPAkeErMS6DLDYxPvQEEkoVRz1",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "L15dTs7zPs6UY2HHBGA8BrhV5gTurDkc6RaYw6ZPtdZptsuPR7K3",
    "private_key": "733134eb516f94aa56ab7ef0874a0d71daf38c5c009dec2a1261861a15889631",
    "wif_type": "wif-compressed",
    "public_key": "02cdcd8f846a73e75c8a845d1df19dc23031648c219d1efc6fe945cd089f3052b0",
    "public_key_type": "compressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "1BPmkfRYzPAkeErMS6DLDYxPvQEEkoVRz1",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseb7ruSNDGP7cmnFHQpmos7TeAy26AFN4GyRTBqq6hiaFbQzQBvirD9oHsafQvzd
Encrypted WIF: {
    "encrypted_wif": "6PoEPBnJjm8UAiSGWQEKKNq9V2GMHqKkTcUqUFzsaX7wgjpQWR2qWPdnpt",
    "confirmation_code": "cfrm38VWx5xH1JFm5EVE3mzQvDPFkz7SqNiaFxhyUfp3Fjc2wdYmK7dGEWoW6irDPSrwoaxB5zS",
    "public_key": "024c5175a177a0b6cf0a3d06065345e2e2d0529ea0191ace3d7b003f304353511b",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "compressed",
    "address": "1MQaLNgukYWRkNgtmc1dzJ13yFvJoW34u4"
}
Confirm Code: {
    "public_key": "024c5175a177a0b6cf0a3d06065345e2e2d0529ea0191ace3d7b003f304353511b",
    "public_key_type": "compressed",
    "address": "1MQaLNgukYWRkNgtmc1dzJ13yFvJoW34u4",
    "lot": 369861,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "KzFbTBirbEEtEPgWL3xhohUcrg6yUmJupAGrid7vBP9F2Vh8GTUB",
    "private_key": "5a7b39eef5d02551b2d362384e57f9823a1c9bed48a260af920a8bb5d6ad971f",
    "wif_type": "wif-compressed",
    "public_key": "024c5175a177a0b6cf0a3d06065345e2e2d0529ea0191ace3d7b003f304353511b",
    "public_key_type": "compressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "1MQaLNgukYWRkNgtmc1dzJ13yFvJoW34u4",
    "lot": 369861,
    "sequence": 1
}
-----------------------------------------------------------------------------------------------------------------------------
```
</details>

## Development

To get started, just fork this repo, clone it locally, and run:

```
pip install -e .[desktop,tests,docs]
```

## Testing

You can run the tests with:

```
pytest
```

Or use `tox` to run the complete suite against the full set of build targets, or pytest to run specific 
tests against a specific version of Python.

## Contributing

Feel free to open an [issue](https://github.com/meherett/python-bip38/issues) if you find a problem,
or a pull request if you've solved an issue. And also any help in testing, development,
documentation and other tasks is highly appreciated and useful to the project.
There are tasks for contributors of all experience levels.

For more information, see the [CONTRIBUTING.md](https://github.com/meherett/python-bip38/blob/master/CONTRIBUTING.md) file.

## Supported Cryptocurrencies

This module supports more than 150+ cryptocurrencies, including the following:

<table><thead><tr><th align='left'><div style="margin: 0;">Name</div></th><th><div style="margin: 0;">Network</div></th><th><div style="margin: 0;">WIF Prefix</div></th><th><div style="margin: 0;">Address Prefix</div></th></tr></thead><tbody><tr><td align='left' rowspan='1'>Adcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb0</code></td><td align='center'><code>0x17</code></td></tr><tr><td align='left' rowspan='1'>Anon</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x582</code></td></tr><tr><td align='left' rowspan='1'>Argoneum</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xbf</code></td><td align='center'><code>0x32</code></td></tr><tr><td align='left' rowspan='1'>Artax</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x97</code></td><td align='center'><code>0x17</code></td></tr><tr><td align='left' rowspan='1'>Aryacoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x97</code></td><td align='center'><code>0x17</code></td></tr><tr><td align='left' rowspan='1'>Asiacoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x97</code></td><td align='center'><code>0x17</code></td></tr><tr><td align='left' rowspan='1'>Auroracoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x97</code></td><td align='center'><code>0x17</code></td></tr><tr><td align='left' rowspan='1'>Avian</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x3c</code></td></tr><tr><td align='left' rowspan='1'>Axe</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xcc</code></td><td align='center'><code>0x37</code></td></tr><tr><td align='left' rowspan='1'>Bata</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xa4</code></td><td align='center'><code>0x19</code></td></tr><tr><td align='left' rowspan='1'>BeetleCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x99</code></td><td align='center'><code>0x1a</code></td></tr><tr><td align='left' rowspan='1'>BelaCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x99</code></td><td align='center'><code>0x19</code></td></tr><tr><td align='left' rowspan='1'>BitCloud</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x99</code></td><td align='center'><code>0x19</code></td></tr><tr><td align='left' rowspan='1'>BitSend</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xcc</code></td><td align='center'><code>0x66</code></td></tr><tr><td align='left' rowspan='3'>Bitcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x00</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x6f</code></td></tr><tr><td align='center'><code>regtest</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x6f</code></td></tr><tr><td align='left' rowspan='1'>BitcoinAtom</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x17</code></td></tr><tr><td align='left' rowspan='1'>BitcoinGold</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x26</code></td></tr><tr><td align='left' rowspan='1'>BitcoinGreen</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x2e</code></td><td align='center'><code>0x26</code></td></tr><tr><td align='left' rowspan='1'>BitcoinPlus</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x99</code></td><td align='center'><code>0x19</code></td></tr><tr><td align='left' rowspan='2'>BitcoinPrivate</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x1325</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x1957</code></td></tr><tr><td align='left' rowspan='1'>BitcoinSV</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x00</code></td></tr><tr><td align='left' rowspan='1'>BitcoinZ</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x1cb8</code></td></tr><tr><td align='left' rowspan='1'>Bitcore</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x03</code></td></tr><tr><td align='left' rowspan='1'>Blackcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x99</code></td><td align='center'><code>0x19</code></td></tr><tr><td align='left' rowspan='1'>BlockStamp</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x00</code></td></tr><tr><td align='left' rowspan='2'>Blocknode</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x4b</code></td><td align='center'><code>0x19</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0x89</code></td><td align='center'><code>0x55</code></td></tr><tr><td align='left' rowspan='1'>Bolivarcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xd5</code></td><td align='center'><code>0x55</code></td></tr><tr><td align='left' rowspan='1'>BritCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x99</code></td><td align='center'><code>0x19</code></td></tr><tr><td align='left' rowspan='1'>CPUChain</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x1c</code></td></tr><tr><td align='left' rowspan='1'>CanadaeCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x9c</code></td><td align='center'><code>0x1c</code></td></tr><tr><td align='left' rowspan='1'>Cannacoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x9c</code></td><td align='center'><code>0x1c</code></td></tr><tr><td align='left' rowspan='1'>Clams</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x85</code></td><td align='center'><code>0x89</code></td></tr><tr><td align='left' rowspan='1'>ClubCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x99</code></td><td align='center'><code>0x1c</code></td></tr><tr><td align='left' rowspan='1'>Compcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x9c</code></td><td align='center'><code>0x1c</code></td></tr><tr><td align='left' rowspan='1'>CranePay</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x7b</code></td><td align='center'><code>0x1c</code></td></tr><tr><td align='left' rowspan='1'>Crave</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x99</code></td><td align='center'><code>0x46</code></td></tr><tr><td align='left' rowspan='2'>Dash</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xcc</code></td><td align='center'><code>0x4c</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x8c</code></td></tr><tr><td align='left' rowspan='1'>DeepOnion</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x9f</code></td><td align='center'><code>0x1f</code></td></tr><tr><td align='left' rowspan='1'>Defcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x9e</code></td><td align='center'><code>0x1e</code></td></tr><tr><td align='left' rowspan='1'>Denarius</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x9e</code></td><td align='center'><code>0x1e</code></td></tr><tr><td align='left' rowspan='1'>Diamond</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xda</code></td><td align='center'><code>0x5a</code></td></tr><tr><td align='left' rowspan='1'>DigiByte</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x1e</code></td></tr><tr><td align='left' rowspan='1'>Digitalcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x9e</code></td><td align='center'><code>0x1e</code></td></tr><tr><td align='left' rowspan='2'>Divi</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xd4</code></td><td align='center'><code>0x1e</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xd4</code></td><td align='center'><code>0x1e</code></td></tr><tr><td align='left' rowspan='2'>Dogecoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xf1</code></td><td align='center'><code>0x1e</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xf1</code></td><td align='center'><code>0x71</code></td></tr><tr><td align='left' rowspan='1'>EDRCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xdd</code></td><td align='center'><code>0x5d</code></td></tr><tr><td align='left' rowspan='1'>Ecoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xdc</code></td><td align='center'><code>0x5c</code></td></tr><tr><td align='left' rowspan='1'>Einsteinium</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xa1</code></td><td align='center'><code>0x21</code></td></tr><tr><td align='left' rowspan='1'>Elastos</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x21</code></td></tr><tr><td align='left' rowspan='1'>Energi</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x6a</code></td><td align='center'><code>0x21</code></td></tr><tr><td align='left' rowspan='1'>EuropeCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xa8</code></td><td align='center'><code>0x21</code></td></tr><tr><td align='left' rowspan='2'>Evrmore</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x21</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x6f</code></td></tr><tr><td align='left' rowspan='1'>ExclusiveCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xa1</code></td><td align='center'><code>0x21</code></td></tr><tr><td align='left' rowspan='2'>FIX</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x3c</code></td><td align='center'><code>0x23</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xed</code></td><td align='center'><code>0x4c</code></td></tr><tr><td align='left' rowspan='1'>Feathercoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x8e</code></td><td align='center'><code>0x0e</code></td></tr><tr><td align='left' rowspan='1'>Firo</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xd2</code></td><td align='center'><code>0x52</code></td></tr><tr><td align='left' rowspan='1'>Firstcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xa3</code></td><td align='center'><code>0x23</code></td></tr><tr><td align='left' rowspan='1'>Flashcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xc4</code></td><td align='center'><code>0x44</code></td></tr><tr><td align='left' rowspan='1'>Flux</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x1cb8</code></td></tr><tr><td align='left' rowspan='2'>Foxdcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x23</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x5f</code></td></tr><tr><td align='left' rowspan='1'>FujiCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xa4</code></td><td align='center'><code>0x24</code></td></tr><tr><td align='left' rowspan='1'>GCRCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x9a</code></td><td align='center'><code>0x26</code></td></tr><tr><td align='left' rowspan='1'>GameCredits</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xa6</code></td><td align='center'><code>0x26</code></td></tr><tr><td align='left' rowspan='1'>GoByte</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xc6</code></td><td align='center'><code>0x26</code></td></tr><tr><td align='left' rowspan='1'>Gridcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xbe</code></td><td align='center'><code>0x3e</code></td></tr><tr><td align='left' rowspan='2'>GroestlCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x24</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x6f</code></td></tr><tr><td align='left' rowspan='1'>Gulden</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x62</code></td><td align='center'><code>0x26</code></td></tr><tr><td align='left' rowspan='1'>Helleniccoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb0</code></td><td align='center'><code>0x30</code></td></tr><tr><td align='left' rowspan='1'>Hempcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xa8</code></td><td align='center'><code>0x28</code></td></tr><tr><td align='left' rowspan='1'>Horizen</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x2089</code></td></tr><tr><td align='left' rowspan='1'>Hush</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x1cb8</code></td></tr><tr><td align='left' rowspan='1'>IXCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x8a</code></td></tr><tr><td align='left' rowspan='1'>InsaneCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x37</code></td><td align='center'><code>0x66</code></td></tr><tr><td align='left' rowspan='1'>InternetOfPeople</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x31</code></td><td align='center'><code>0x75</code></td></tr><tr><td align='left' rowspan='1'>Jumbucks</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xab</code></td><td align='center'><code>0x2b</code></td></tr><tr><td align='left' rowspan='1'>Kobocoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xa3</code></td><td align='center'><code>0x23</code></td></tr><tr><td align='left' rowspan='1'>Komodo</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xbc</code></td><td align='center'><code>0x3c</code></td></tr><tr><td align='left' rowspan='1'>LBRYCredits</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x1c</code></td><td align='center'><code>0x55</code></td></tr><tr><td align='left' rowspan='1'>Landcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb0</code></td><td align='center'><code>0x30</code></td></tr><tr><td align='left' rowspan='1'>Linx</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xcb</code></td><td align='center'><code>0x4b</code></td></tr><tr><td align='left' rowspan='2'>Litecoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb0</code></td><td align='center'><code>0x30</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x6f</code></td></tr><tr><td align='left' rowspan='1'>LitecoinCash</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb0</code></td><td align='center'><code>0x1c</code></td></tr><tr><td align='left' rowspan='1'>LitecoinZ</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0xab3</code></td></tr><tr><td align='left' rowspan='1'>Lkrcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb0</code></td><td align='center'><code>0x30</code></td></tr><tr><td align='left' rowspan='1'>Lynx</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xad</code></td><td align='center'><code>0x2d</code></td></tr><tr><td align='left' rowspan='1'>Mazacoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xe0</code></td><td align='center'><code>0x32</code></td></tr><tr><td align='left' rowspan='1'>Megacoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb2</code></td><td align='center'><code>0x32</code></td></tr><tr><td align='left' rowspan='1'>Minexcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x4b</code></td></tr><tr><td align='left' rowspan='1'>Monacoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb0</code></td><td align='center'><code>0x32</code></td></tr><tr><td align='left' rowspan='1'>Monk</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x37</code></td><td align='center'><code>0x33</code></td></tr><tr><td align='left' rowspan='1'>Myriadcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb2</code></td><td align='center'><code>0x32</code></td></tr><tr><td align='left' rowspan='1'>NIX</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x26</code></td></tr><tr><td align='left' rowspan='1'>Namecoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x34</code></td></tr><tr><td align='left' rowspan='1'>Navcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x96</code></td><td align='center'><code>0x35</code></td></tr><tr><td align='left' rowspan='1'>Neblio</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb5</code></td><td align='center'><code>0x35</code></td></tr><tr><td align='left' rowspan='1'>Neoscoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb1</code></td><td align='center'><code>0x35</code></td></tr><tr><td align='left' rowspan='1'>Neurocoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb5</code></td><td align='center'><code>0x35</code></td></tr><tr><td align='left' rowspan='1'>NewYorkCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xbc</code></td><td align='center'><code>0x3c</code></td></tr><tr><td align='left' rowspan='1'>Novacoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x88</code></td><td align='center'><code>0x08</code></td></tr><tr><td align='left' rowspan='1'>NuBits</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x96</code></td><td align='center'><code>0x19</code></td></tr><tr><td align='left' rowspan='1'>NuShares</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x95</code></td><td align='center'><code>0x3f</code></td></tr><tr><td align='left' rowspan='1'>OKCash</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x03</code></td><td align='center'><code>0x37</code></td></tr><tr><td align='left' rowspan='2'>Omni</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x00</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x6f</code></td></tr><tr><td align='left' rowspan='1'>Onix</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xcb</code></td><td align='center'><code>0x4b</code></td></tr><tr><td align='left' rowspan='1'>Particl</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x6c</code></td><td align='center'><code>0x38</code></td></tr><tr><td align='left' rowspan='1'>Peercoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb7</code></td><td align='center'><code>0x37</code></td></tr><tr><td align='left' rowspan='1'>Pesobit</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb7</code></td><td align='center'><code>0x37</code></td></tr><tr><td align='left' rowspan='1'>Phore</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xd4</code></td><td align='center'><code>0x37</code></td></tr><tr><td align='left' rowspan='1'>Pinkcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x83</code></td><td align='center'><code>0x03</code></td></tr><tr><td align='left' rowspan='2'>Pivx</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xd4</code></td><td align='center'><code>0x1e</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x8b</code></td></tr><tr><td align='left' rowspan='1'>PoSWCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb7</code></td><td align='center'><code>0x37</code></td></tr><tr><td align='left' rowspan='1'>Potcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb7</code></td><td align='center'><code>0x37</code></td></tr><tr><td align='left' rowspan='1'>ProjectCoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x75</code></td><td align='center'><code>0x37</code></td></tr><tr><td align='left' rowspan='1'>Putincoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb7</code></td><td align='center'><code>0x37</code></td></tr><tr><td align='left' rowspan='2'>Qtum</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x3a</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x78</code></td></tr><tr><td align='left' rowspan='2'>RSK</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x00</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x6f</code></td></tr><tr><td align='left' rowspan='1'>Rapids</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x2e</code></td><td align='center'><code>0x3d</code></td></tr><tr><td align='left' rowspan='2'>Ravencoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x3c</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x6f</code></td></tr><tr><td align='left' rowspan='1'>Reddcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xbd</code></td><td align='center'><code>0x3d</code></td></tr><tr><td align='left' rowspan='1'>Ripple</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x00</code></td></tr><tr><td align='left' rowspan='1'>Ritocoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x8b</code></td><td align='center'><code>0x19</code></td></tr><tr><td align='left' rowspan='1'>Rubycoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xbc</code></td><td align='center'><code>0x3c</code></td></tr><tr><td align='left' rowspan='1'>Safecoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xbd</code></td><td align='center'><code>0x3d</code></td></tr><tr><td align='left' rowspan='1'>Saluscoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xbf</code></td><td align='center'><code>0x3f</code></td></tr><tr><td align='left' rowspan='1'>Scribe</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x6e</code></td><td align='center'><code>0x3c</code></td></tr><tr><td align='left' rowspan='2'>ShadowCash</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xbf</code></td><td align='center'><code>0x3f</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xff</code></td><td align='center'><code>0x7f</code></td></tr><tr><td align='left' rowspan='2'>Slimcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x46</code></td><td align='center'><code>0x3f</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0x57</code></td><td align='center'><code>0x6f</code></td></tr><tr><td align='left' rowspan='1'>Smileycoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x05</code></td><td align='center'><code>0x19</code></td></tr><tr><td align='left' rowspan='1'>Solarcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x92</code></td><td align='center'><code>0x12</code></td></tr><tr><td align='left' rowspan='2'>Stash</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xcc</code></td><td align='center'><code>0x4c</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x8c</code></td></tr><tr><td align='left' rowspan='2'>Stratis</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xbf</code></td><td align='center'><code>0x3f</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xbf</code></td><td align='center'><code>0x41</code></td></tr><tr><td align='left' rowspan='2'>Sugarchain</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x3f</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x42</code></td></tr><tr><td align='left' rowspan='1'>Syscoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x3f</code></td></tr><tr><td align='left' rowspan='1'>TOACoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xc1</code></td><td align='center'><code>0x41</code></td></tr><tr><td align='left' rowspan='2'>TWINS</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x42</code></td><td align='center'><code>0x49</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xed</code></td><td align='center'><code>0x4c</code></td></tr><tr><td align='left' rowspan='1'>ThoughtAI</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x7b</code></td><td align='center'><code>0x07</code></td></tr><tr><td align='left' rowspan='1'>UltimateSecureCash</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xbf</code></td><td align='center'><code>0x44</code></td></tr><tr><td align='left' rowspan='1'>Unobtanium</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xe0</code></td><td align='center'><code>0x82</code></td></tr><tr><td align='left' rowspan='1'>Vcash</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xc7</code></td><td align='center'><code>0x47</code></td></tr><tr><td align='left' rowspan='1'>Verge</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x9e</code></td><td align='center'><code>0x1e</code></td></tr><tr><td align='left' rowspan='1'>Vertcoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x47</code></td></tr><tr><td align='left' rowspan='2'>Viacoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xc7</code></td><td align='center'><code>0x47</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xff</code></td><td align='center'><code>0x7f</code></td></tr><tr><td align='left' rowspan='1'>VirtualCash</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xc7</code></td><td align='center'><code>0x47</code></td></tr><tr><td align='left' rowspan='1'>Vivo</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xc6</code></td><td align='center'><code>0x46</code></td></tr><tr><td align='left' rowspan='1'>Voxels</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xc6</code></td><td align='center'><code>0x46</code></td></tr><tr><td align='left' rowspan='1'>Wagerr</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xc7</code></td><td align='center'><code>0x49</code></td></tr><tr><td align='left' rowspan='1'>Whitecoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xc9</code></td><td align='center'><code>0x49</code></td></tr><tr><td align='left' rowspan='1'>Wincoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xc9</code></td><td align='center'><code>0x49</code></td></tr><tr><td align='left' rowspan='1'>XUEZ</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xd4</code></td><td align='center'><code>0x4b</code></td></tr><tr><td align='left' rowspan='1'>Ycash</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x1c28</code></td></tr><tr><td align='left' rowspan='1'>ZClassic</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x1cb8</code></td></tr><tr><td align='left' rowspan='2'>Zcash</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x1cb8</code></td></tr><tr><td align='center'><code>testnet</code></td><td align='center'><code>0xef</code></td><td align='center'><code>0x1d25</code></td></tr><tr><td align='left' rowspan='1'>Zetacoin</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xe0</code></td><td align='center'><code>0x50</code></td></tr><tr><td align='left' rowspan='1'>ZooBC</td><td align='center'><code>mainnet</code></td><td align='center'><code>0x80</code></td><td align='center'><code>0x00</code></td></tr><tr><td align='left' rowspan='1'>eGulden</td><td align='center'><code>mainnet</code></td><td align='center'><code>0xb0</code></td><td align='center'><code>0x30</code></td></tr></tbody></table>

## Donations

Buy me a coffee if You found this tool helpful:

- **Bitcoin** - 16c7ajUwHEMaafrceuYSrd35SDjmfVdjoS
- **Ethereum / ERC20** - 0xD3cbCB0B6F82A03C715D665b72dC44CEf54e6D9B

Thank you very much for your support.

## License

Distributed under the [MIT](https://github.com/meherett/python-bip38/blob/master/LICENSE) license. See ``LICENSE`` for more information.
