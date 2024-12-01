===========================================
Bitcoin Improvement Proposal - 0038 / BIP38
===========================================

|Build Status| |PyPI Version| |Documentation Status| |PyPI License| |PyPI Python Version| |Coverage Status|

.. |Build Status| image:: https://img.shields.io/github/actions/workflow/status/talonlab/python-bip38/build.yml
   :target: https://github.com/talonlab/python-bip38/actions/workflows/build.yml

.. |PyPI Version| image:: https://img.shields.io/pypi/v/bip38.svg?color=blue
   :target: https://pypi.org/project/bip38

.. |Documentation Status| image:: https://readthedocs.org/projects/bip38/badge/?version=master
   :target: https://bip38.readthedocs.io/en/master/?badge=master

.. |PyPI License| image:: https://img.shields.io/pypi/l/bip38?color=black
   :target: https://pypi.org/project/bip38

.. |PyPI Python Version| image:: https://img.shields.io/pypi/pyversions/bip38.svg
   :target: https://pypi.org/project/bip38

.. |Coverage Status| image:: https://coveralls.io/repos/github/talonlab/python-bip38/badge.svg?branch=master
   :target: https://coveralls.io/github/talonlab/python-bip38?branch=master

A Python library for the implementation of Bitcoin Improvement Proposal - 0038 / (BIP38) protocol.
This library supports both `No EC-multiply <https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki#encryption-when-ec-multiply-flag-is-not-used>`_ and `EC-multiply <https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki#encryption-when-ec-multiply-mode-is-used>`_ modes and is compatible with over 150+ cryptocurrencies.
It's specifically tailored for Pay-to-PubKey-Hash (P2PKH) address types.

For more info see the `Passphrase-protected private key - BIP38 <https://en.bitcoin.it/wiki/BIP_0038>`_ specs.

Installing BIP38
================

The easiest way to install ``bip38`` is via pip:

::

    pip install bip38


If you want to run the latest version of the code, you can install from git:

::

    pip install git+ssh://github.com/talonlab/python-bip38.git


For the versions available, see the `tags on this repository <https://github.com/talonlab/python-bip38/tags>`_.

Quick Usage
===========

no EC multiply:
_______________

::

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


.. raw:: html

   <details open>
        <summary>Output</summary>

.. code-block:: shell

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

.. raw:: html

   </details>


EC multiply:
------------

::

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

.. raw:: html

   <details>
        <summary>Output</summary>

.. code-block:: shell

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

.. raw:: html

   </details>


Development
===========

We welcome pull requests. To get started, just fork this `github repository <https://github.com/talonlab/python-bip38>`_, clone it locally, and run:

::

    pip install -e .[tests,docs]


Testing
=======

You can run the tests with:

::

    pytest


Or use **tox** to run the complete suite against the full set of build targets, or pytest to run specific
tests against a specific version of Python.


Contributing
============

Feel free to open an `issue <https://github.com/talonlab/python-bip38/issues>`_ if you find a problem,
or a pull request if you've solved an issue. And also any help in testing, development,
documentation and other tasks is highly appreciated and useful to the project.
There are tasks for contributors of all experience levels.

For more information, see the `CONTRIBUTING.md <https://github.com/talonlab/python-bip38/blob/master/CONTRIBUTING.md>`_ file.

Donations
=========

Buy me a coffee if You found this tool helpful:

- **Bitcoin** - 16c7ajUwHEMaafrceuYSrd35SDjmfVdjoS
- **Ethereum / Tether** - 0xD3cbCB0B6F82A03C715D665b72dC44CEf54e6D9B
- **Solana** - 9cVoan5GvnpVvysEkFWEFR4k9cpTdWKmqQ6Gi7nwM5ES

Thank you very much for your support.


License
=======

Distributed under the `MIT <https://github.com/talonlab/python-bip38/blob/master/LICENSE>`_ license. See **LICENSE** for more information.
