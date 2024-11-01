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
PASSPHRASE: str = "bip38"  # u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
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
WIF: 5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR
BIP38 Encrypted WIF: 6PRVWUbm1BX3fNUTgZoCYj9VLAQzxB9daqVfr4TgbhxegTKoSz9jRDks9a
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
WIF: L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP
BIP38 Encrypted WIF: 6PYNKZ1EBitZbP8ctdXG5xkpsFAtgd7c9JQdLCXqbhBRbANSnuUK6PgQdV
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
PASSPHRASE: str = "bip38"  # u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
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
Intermediate Passphrase: passphrasemG6Ae7PYWEuso54V4dMKFK7mpFPz4t1T1BhywtvNVt7E4xDM8Vq8xo68K1DdW9
Encrypted WIF: {
    "encrypted_wif": "6PfQma2dv1Hov8kSobbZapHKA69g96oGWA8rwfcDP4ZKs4ncqPeJP23qnL",
    "confirmation_code": "cfrm38V5Txsng8kFerZPprMH9LjHnDTv22JzroUqHwZN1B9xxoB6PU3UtC5o12wZspe21Uec33W",
    "public_key": "049a25850934fd16bc108046a60794a18cf27ec32f1ad5de75d6571aecc889ff7f30135195c69931115a9f2bf4262ee1dba707021dacd4e0bf68da195f60727643",
    "seed": "d937267be638947d6dc7971f9781ce61076847b490b2dd06",
    "public_key_type": "uncompressed",
    "address": "1QAWVYDpESZ2afxFnbWS5G64EQfzo2imNR"
}
Confirm Code: {
    "public_key": "049a25850934fd16bc108046a60794a18cf27ec32f1ad5de75d6571aecc889ff7f30135195c69931115a9f2bf4262ee1dba707021dacd4e0bf68da195f60727643",
    "public_key_type": "uncompressed",
    "address": "1QAWVYDpESZ2afxFnbWS5G64EQfzo2imNR",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "5KXXTS7ULYo1kxgirDgRfzviTEocKGLtTV9SUHHbRb7z2AEVYVB",
    "private_key": "e155b57cb4d94ef4d2b5c32879ffaad851da0b20a10deb392c31404cc29637a4",
    "wif_type": "wif",
    "public_key": "049a25850934fd16bc108046a60794a18cf27ec32f1ad5de75d6571aecc889ff7f30135195c69931115a9f2bf4262ee1dba707021dacd4e0bf68da195f60727643",
    "public_key_type": "uncompressed",
    "seed": "d937267be638947d6dc7971f9781ce61076847b490b2dd06",
    "address": "1QAWVYDpESZ2afxFnbWS5G64EQfzo2imNR",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseeX6YjBj1AXhiw28iQfnn1d5N6Lsf3crrsmxQMaHco4Kpzoymah46hP5bbQqRva
Encrypted WIF: {
    "encrypted_wif": "6PgRJMfKzjt6puxjobszrdtDa4KeRT5dRNwSaqj8BtQAvsUJLz7XifLqxf",
    "confirmation_code": "cfrm38V8kgweU6FKDGY1pMtucLfBTp5bD3QMd64GmRJtVR8ifZaynoLDW8kHY9rACq3Xvrdpe2R",
    "public_key": "040bf1d82b01b2691aaf143991dbaf3cea58cafd74b4377536a1f4da684151151c44118b137652df3bc328c7bb07b9aefa94a6194e8a1b9034265100df99740819",
    "seed": "73123c97834cc52fe937e29d33b86a12085a241e347dffc5",
    "public_key_type": "uncompressed",
    "address": "1Pd8Scd8KfhzLSzyLgMgLKc58tk9f3dnD5"
}
Confirm Code: {
    "public_key": "040bf1d82b01b2691aaf143991dbaf3cea58cafd74b4377536a1f4da684151151c44118b137652df3bc328c7bb07b9aefa94a6194e8a1b9034265100df99740819",
    "public_key_type": "uncompressed",
    "address": "1Pd8Scd8KfhzLSzyLgMgLKc58tk9f3dnD5",
    "lot": 863741,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "5J3W72BqJ7YFEkJR8KuGmHRXdr8AJUnKT1oKp6hQAtx8bKVgmqU",
    "private_key": "1e0223706880eebc96470b0629262e31a828992e0f531c6e4793cfee9d30a694",
    "wif_type": "wif",
    "public_key": "040bf1d82b01b2691aaf143991dbaf3cea58cafd74b4377536a1f4da684151151c44118b137652df3bc328c7bb07b9aefa94a6194e8a1b9034265100df99740819",
    "public_key_type": "uncompressed",
    "seed": "73123c97834cc52fe937e29d33b86a12085a241e347dffc5",
    "address": "1Pd8Scd8KfhzLSzyLgMgLKc58tk9f3dnD5",
    "lot": 863741,
    "sequence": 1
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseoCyP3atnoAxv9o8Nhfi7S6fsucu46s9wpDxS4cBGeVPhNQxSBrps3yR4P4Z7Mk
Encrypted WIF: {
    "encrypted_wif": "6PnR1W6XPrx6RK4mgGCjwx3c24zs6peuyBiiKoYfwGpWoJw8A9HeiGz1wf",
    "confirmation_code": "cfrm38VUHiVy4jMqxJHqQdsuaLkMN3LxdseumiHcQQMCnnYaRtkZ5oQEtfWdhnbGCjV1hXU7zqc",
    "public_key": "02b12e27280a74e55d979d23eb2dc4c107028236512bdbdbed3ba0d3c139500522",
    "seed": "ab0ed77af04c331801afcf61a27c787e7e27de179230d41e",
    "public_key_type": "compressed",
    "address": "17vbPdAUMftcA5qHXTVS6KiAWh3psHq8Kn"
}
Confirm Code: {
    "public_key": "02b12e27280a74e55d979d23eb2dc4c107028236512bdbdbed3ba0d3c139500522",
    "public_key_type": "compressed",
    "address": "17vbPdAUMftcA5qHXTVS6KiAWh3psHq8Kn",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "L4bxdGanNrHTkDHzQWAwn7y8KhVzAsuuXUzqK8Ah6822MbTy9HMt",
    "private_key": "dc4eb85c52ad9d82152a0ecd9542202a164556eb1f444a59da5936269527278e",
    "wif_type": "wif-compressed",
    "public_key": "02b12e27280a74e55d979d23eb2dc4c107028236512bdbdbed3ba0d3c139500522",
    "public_key_type": "compressed",
    "seed": "ab0ed77af04c331801afcf61a27c787e7e27de179230d41e",
    "address": "17vbPdAUMftcA5qHXTVS6KiAWh3psHq8Kn",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphrasedCiMgYvgiaHcR6kGF5SLANuCte7ggrupYpsLbe9kNtmqx4XQF2LGBiPZSbwGWk
Encrypted WIF: {
    "encrypted_wif": "6PoNSsfzTSpKZreygc8DVCMTjFXVwMNw6ddpXSCkgYYWw3uHNXs2BRkx8M",
    "confirmation_code": "cfrm38VXQMwDqnPHg3NB2G35qxgadVCfoC5SjntbhaBxAe5VX9sasVHqQHKV44XLLpJqy2z4iu6",
    "public_key": "033c0c467652bb0f8227c014551af8cc3cd4c4f0984f712ddc94dc49723370b8e7",
    "seed": "bad4ce4f6e1a6aa226cd89602d92c636d4ab23891808cc6e",
    "public_key_type": "compressed",
    "address": "1JkLXpEAwGBcViwwVDXfiURfd4dg8A4Qos"
}
Confirm Code: {
    "public_key": "033c0c467652bb0f8227c014551af8cc3cd4c4f0984f712ddc94dc49723370b8e7",
    "public_key_type": "compressed",
    "address": "1JkLXpEAwGBcViwwVDXfiURfd4dg8A4Qos",
    "lot": 863741,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "L4KTQ9h5uUWy6r4tXC1wDCfGJbB31nX4Wmfz6FKHAjGxncnBLoh4",
    "private_key": "d3d13893951d6256e5633f6a003936214c4b0e9f1211682af1df858464d9ea52",
    "wif_type": "wif-compressed",
    "public_key": "033c0c467652bb0f8227c014551af8cc3cd4c4f0984f712ddc94dc49723370b8e7",
    "public_key_type": "compressed",
    "seed": "bad4ce4f6e1a6aa226cd89602d92c636d4ab23891808cc6e",
    "address": "1JkLXpEAwGBcViwwVDXfiURfd4dg8A4Qos",
    "lot": 863741,
    "sequence": 1
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseondJwvQGEWFNrMBiUhdVNwLNdPDHBRrVZkVuH3dVubC4JcuxLnKWFep8uGwhth
Encrypted WIF: {
    "encrypted_wif": "6PfXN4Up17PgFdoxEBVwAxRuaQ1UderDKQ2q6nGCrhLVPD7GS3awBfKtox",
    "confirmation_code": "cfrm38V5qTEpyzqDDgry1mEmRPEn4xaXC74tKbH9jfSpHkfiud3SW9dRSmhZHuTwvW78eVUWwjx",
    "public_key": "04bc2b0adc1106e45fa86a3507cbec5bc834c33780c7ae774b885ac50c8489fc481ae5198457e5733e3f91e2b68df10ba55fa0408a918e4f37e475591cfa41d31d",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "uncompressed",
    "address": "12NzK7AbrtY5evVfDb7nnM5DNtbjGKBB6g"
}
Confirm Code: {
    "public_key": "04bc2b0adc1106e45fa86a3507cbec5bc834c33780c7ae774b885ac50c8489fc481ae5198457e5733e3f91e2b68df10ba55fa0408a918e4f37e475591cfa41d31d",
    "public_key_type": "uncompressed",
    "address": "12NzK7AbrtY5evVfDb7nnM5DNtbjGKBB6g",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "5KZ2wb3ANziUbxcxLDq6nK854r6wF3qnxvk6rBVnKhdrRS3YcHb",
    "private_key": "e4c27e23f2b243ca0cea2695362a48aaefba35951bcbaad9ebab1d7ab2a1b8e9",
    "wif_type": "wif",
    "public_key": "04bc2b0adc1106e45fa86a3507cbec5bc834c33780c7ae774b885ac50c8489fc481ae5198457e5733e3f91e2b68df10ba55fa0408a918e4f37e475591cfa41d31d",
    "public_key_type": "uncompressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "12NzK7AbrtY5evVfDb7nnM5DNtbjGKBB6g",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseb7ruSNPsLdQF6TuHGftP9MBJM9mzUFqEpr37Quzua67SzYyhXtgGg32Ukkif4w
Encrypted WIF: {
    "encrypted_wif": "6PgD5Q4BChU5kScKdbcbmdUtkEu9fBTDkB6EHmErH4kRyzveKRodpHzimL",
    "confirmation_code": "cfrm38V84rmYgaHJLLMVTcRmZwnBF7Jj9gShJpWMfsM16r7DS1paysBseVo7WhJ7BwZUfh9ts8a",
    "public_key": "0433f3d09ee3059b559194833063993626c6ce1bb25c3d3ee4e9b2d02ff7c3c6206d526a30d072c167176af1c45bf7331057c2ebc6701e3aebb74acdb3c2b9a5e5",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "uncompressed",
    "address": "1NwyXJShcScbkpB9dUwPqR3fv39Krt9xqH"
}
Confirm Code: {
    "public_key": "0433f3d09ee3059b559194833063993626c6ce1bb25c3d3ee4e9b2d02ff7c3c6206d526a30d072c167176af1c45bf7331057c2ebc6701e3aebb74acdb3c2b9a5e5",
    "public_key_type": "uncompressed",
    "address": "1NwyXJShcScbkpB9dUwPqR3fv39Krt9xqH",
    "lot": 567885,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "5JdgMq9wsmqtMJ7YD5vahf89vgHQgeAqJieAP2h664vUqxhMriv",
    "private_key": "6b9c6a32ae3b9d5fc2050f69e9f9825fece3276e3c979ae16e20c12f971de115",
    "wif_type": "wif",
    "public_key": "0433f3d09ee3059b559194833063993626c6ce1bb25c3d3ee4e9b2d02ff7c3c6206d526a30d072c167176af1c45bf7331057c2ebc6701e3aebb74acdb3c2b9a5e5",
    "public_key_type": "uncompressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "1NwyXJShcScbkpB9dUwPqR3fv39Krt9xqH",
    "lot": 567885,
    "sequence": 1
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseondJwvQGEWFNrMBiUhdVNwLNdPDHBRrVZkVuH3dVubC4JcuxLnKWFep8uGwhth
Encrypted WIF: {
    "encrypted_wif": "6PnYeWbwUScx6DctoFqiJW2vDmsWCT6cVfwmjQXu8aTKLQ2aZfmin6RH6R",
    "confirmation_code": "cfrm38VUic4gbBuLjvrDaXgwMeK42YR5zGLjpgNDF6p7Ro4EVAe9HkeDhzNZxJU9PCJ7PsbHy5s",
    "public_key": "03bc2b0adc1106e45fa86a3507cbec5bc834c33780c7ae774b885ac50c8489fc48",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "compressed",
    "address": "1AUJ4rSiyRd7CmHo6K6n12QPpa1vKW2LaG"
}
Confirm Code: {
    "public_key": "03bc2b0adc1106e45fa86a3507cbec5bc834c33780c7ae774b885ac50c8489fc48",
    "public_key_type": "compressed",
    "address": "1AUJ4rSiyRd7CmHo6K6n12QPpa1vKW2LaG",
    "lot": null,
    "sequence": null
}
BIP38 Decrypted: {
    "wif": "L4tPZwEYQ5k4qJVhDqdJWzzCwyjCR1YMsrDEp5L33YMf8eKHmk5o",
    "private_key": "e4c27e23f2b243ca0cea2695362a48aaefba35951bcbaad9ebab1d7ab2a1b8e9",
    "wif_type": "wif-compressed",
    "public_key": "03bc2b0adc1106e45fa86a3507cbec5bc834c33780c7ae774b885ac50c8489fc48",
    "public_key_type": "compressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "1AUJ4rSiyRd7CmHo6K6n12QPpa1vKW2LaG",
    "lot": null,
    "sequence": null
}
-----------------------------------------------------------------------------------------------------------------------------
Intermediate Passphrase: passphraseb7ruSNDGP7cmpocKZC2U6hDfT4dFEPB2dpdr9UNjwwUW2tSYkKukFv4JNYnXAs
Encrypted WIF: {
    "encrypted_wif": "6PoG6xLK7sgeZP8gPzNmFvmp4serw1MTprunK29YwbwnxsnU7Jmb6EpHqs",
    "confirmation_code": "cfrm38VX3h421KiP57NBU3ohrBh1bAgBbMvqntvcqw6wfgq9EaBmDJxLx3Mq6hTmRxBnLzQa8kR",
    "public_key": "03bf9c150cef682e643e4745a4bba70fd183bf1726e3dd45d76fef599b39a3e1fc",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "public_key_type": "compressed",
    "address": "15u9QmfwXC5Hi9mK9qwHCuCdGCw1rPwmug"
}
Confirm Code: {
    "public_key": "03bf9c150cef682e643e4745a4bba70fd183bf1726e3dd45d76fef599b39a3e1fc",
    "public_key_type": "compressed",
    "address": "15u9QmfwXC5Hi9mK9qwHCuCdGCw1rPwmug",
    "lot": 369861,
    "sequence": 1
}
BIP38 Decrypted: {
    "wif": "L1HftYcdEQ3D7Vn6f1psXumjY5PLdtGLx781C2bLnzZcPFTM7gDQ",
    "private_key": "7963113c7ec95bedb41d415e393ea07edcdb2fe9ab080faededd38b210b320ff",
    "wif_type": "wif-compressed",
    "public_key": "03bf9c150cef682e643e4745a4bba70fd183bf1726e3dd45d76fef599b39a3e1fc",
    "public_key_type": "compressed",
    "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c",
    "address": "15u9QmfwXC5Hi9mK9qwHCuCdGCw1rPwmug",
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
