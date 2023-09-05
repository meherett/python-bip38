===============================
Bitcoin Improvement Proposal 38
===============================

|Build Status| |PyPI Version| |Documentation Status| |PyPI License| |PyPI Python Version| |Coverage Status|

.. |Build Status| image:: https://travis-ci.org/meherett/python-bip38.svg?branch=master
   :target: https://travis-ci.org/meherett/python-bip38?branch=master

.. |PyPI Version| image:: https://img.shields.io/pypi/v/bip38.svg?color=blue
   :target: https://pypi.org/project/bip38

.. |Documentation Status| image:: https://readthedocs.org/projects/bip38/badge/?version=master
   :target: https://bip38.readthedocs.io/en/master/?badge=master

.. |PyPI License| image:: https://img.shields.io/pypi/l/bip38?color=black
   :target: https://pypi.org/project/bip38

.. |PyPI Python Version| image:: https://img.shields.io/pypi/pyversions/bip38.svg
   :target: https://pypi.org/project/bip38

.. |Coverage Status| image:: https://coveralls.io/repos/github/meherett/python-bip38/badge.svg?branch=master
   :target: https://coveralls.io/github/meherett/python-bip38?branch=master

A pure python library for implementation of Bitcoin Improvement Proposal - 0038 / BIP38 protocol. It supports both `No EC-multiply <https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki#encryption-when-ec-multiply-flag-is-not-used>`_ and `EC-multiply <https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki#encryption-when-ec-multiply-mode-is-used>`_ modes.

BIP38 is a cryptographic standard that defines a method for encrypting and securing private keys associated with Bitcoin addresses. It provides a way to create encrypted versions of private keys, which can then be decrypted using a passphrase. This adds an additional layer of security to the process of storing and transmitting private keys.

By encrypting a private key with BIP38, users can protect their funds even if the encrypted private key is exposed. This is because an attacker would need to know the passphrase in order to decrypt the private key and gain access to the associated funds. BIP38 encryption is often used to create "paper wallets" or physical copies of Bitcoin private keys that can be stored offline for enhanced security.

For more info see the `BIP38 <https://en.bitcoin.it/wiki/BIP_0038>`_ specs.

Installing BIP38
================

The easiest way to install ``bip38`` is via pip:

::

    pip install bip38


If you want to run the latest version of the code, you can install from git:

::

    pip install git+git://github.com/meherett/python-bip38.git


For the versions available, see the `tags on this repository <https://github.com/meherett/python-bip38/tags>`_.

Quick Usage
===========

For no EC multiply:
___________________

::

    #!/usr/bin/env python3

    from bip38 import (
        bip38_encrypt, bip38_decrypt
    )

    import json

    # Passphrase / password
    PASSPHRASE: str = "meherett"  # u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
    # Wallet important format's
    WIFs: dict = {
        "wif": "5KN7MzqK5wt2TP1fQCYyHBtDrXdJuXbUzm4A9rKAteGu3Qi5CVR",  # No compression
        "wif-compressed": "L44B5gGEpqEDRS9vVPz7QT35jcBG2r3CZwSwQ4fCewXAhAhqGVpP"  # Compression
    }
    # To show detail
    DETAIL: bool = True

    for WIF in WIFs.keys():

        print("WFI:", WIFs[WIF])
        encrypted_wif: str = bip38_encrypt(
            wif=WIFs[WIF], passphrase=PASSPHRASE
        )
        print("BIP38 Encrypted WIF:", encrypted_wif)
        print("BIP38 Decrypted:", json.dumps(bip38_decrypt(
            encrypted_wif=encrypted_wif, passphrase=PASSPHRASE, detail=DETAIL
        ), indent=4), "\n")


.. raw:: html

   <details open>
        <summary>Output</summary>

.. code-block:: shell

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

.. raw:: html

   </details>


For EC multiply:
----------------

::

    #!/usr/bin/env python3

    from bip38 import (
        intermediate_code, create_new_encrypted_wif, confirm_code, bip38_decrypt
    )
    from typing import List

    import json
    import os

    # Passphrase / password
    PASSPHRASE: str = "meherett"  # u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
    # To show detail
    DETAIL: bool = True
    # List of samples with owner salt, seed, public key type, lot, and sequence
    samples: List[dict] = [
        # Random owner salt & seed, No compression, No lot & sequence
        {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "uncompressed", "lot": None, "sequence": None},
        # Random owner salt & seed, No compression, With lot & sequence
        {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "uncompressed", "lot": 863741, "sequence": 1},
        # Random owner salt & seed, Compression, No lot & sequence
        {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "compressed", "lot": None, "sequence": None},
        # Random owner salt & seed, Compression, With lot & sequence
        {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "compressed", "lot": 863741, "sequence": 1},
        # With owner salt & seed, No compression, No lot & sequence
        {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "uncompressed", "lot": None,
         "sequence": None},
        # With owner salt & seed, No compression, With lot & sequence
        {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "uncompressed", "lot": 567885,
         "sequence": 1},
        # With owner salt & seed, Compression, No lot & sequence
        {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "compressed", "lot": None,
         "sequence": None},
        # With owner salt & seed, Compression, With lot & sequence
        {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "compressed", "lot": 369861,
         "sequence": 1},
    ]

    for sample in samples:

        intermediate_passphrase: str = intermediate_code(
            passphrase=PASSPHRASE, owner_salt=sample["owner_salt"], lot=sample["lot"], sequence=sample["sequence"]
        )

        print("Intermediate Passphrase:", intermediate_passphrase)

        encrypted_wif: dict = create_new_encrypted_wif(
            intermediate_passphrase=intermediate_passphrase, public_key_type=sample["public_key_type"], seed=sample["seed"]
        )
        print("Encrypted WIF:", json.dumps(encrypted_wif, indent=4))

        print("Confirm Code:", json.dumps(confirm_code(
            passphrase=PASSPHRASE, confirmation_code=encrypted_wif["confirmation_code"], detail=DETAIL
        ), indent=4))

        print("BIP38 Decrypted:", json.dumps(bip38_decrypt(
            encrypted_wif=encrypted_wif["encrypted_wif"], passphrase=PASSPHRASE, detail=DETAIL
        ), indent=4))

        print("-" * 50)

.. raw:: html

   <details>
        <summary>Output</summary>

.. code-block:: shell

    Intermediate Passphrase: passphraseoouQoiPKqUgnkxc4ZMMZoujRuZ9AxeeG5j53UwbCHCf1UToFvAV1rVDCJdypwL
    Encrypted WIF: {
        "encrypted_wif": "6PfNDqSUS9n8G6kjfPXW5jbKFS9QRVfRSjSoyxgwKPiBKHQrywNSYt2X5U",
        "confirmation_code": "cfrm38V5KfUeoryRMPjAaHKLk2ZYyyoHttAdHnMe3MhHvmPcuYLkgxDpW7og9kdZyg1HG4ae6JU",
        "public_key": "0492ce7005e0fd9a218325447489f1eff6d487dd9d2e5d501302943485217e4c9411a8dfea9d803a14c526ea537b2b2683e5ef8c33660622847cbfd8979433d512",
        "seed": "357f1c58ca068ebfda512ff1dbc85f19e260e798344c9232",
        "public_key_type": "uncompressed",
        "address": "1EV1hewDjJ7YJut2eZ2gruDFcVhRN5qrXq"
    }
    Confirm Code: {
        "public_key": "0492ce7005e0fd9a218325447489f1eff6d487dd9d2e5d501302943485217e4c9411a8dfea9d803a14c526ea537b2b2683e5ef8c33660622847cbfd8979433d512",
        "public_key_type": "uncompressed",
        "address": "1EV1hewDjJ7YJut2eZ2gruDFcVhRN5qrXq",
        "lot": null,
        "sequence": null
    }
    BIP38 Decrypted: {
        "wif": "5JzxQcXyrqqep2unYkugwsVDWYvG5mNFpJJHE4MQoxw8wFxfumg",
        "private_key": "9bec1d3c0fa418d5a2e7ac3a2db2644ecc282288feb5c5e12172b62a7fc6c74b",
        "wif_type": "wif",
        "public_key": "0492ce7005e0fd9a218325447489f1eff6d487dd9d2e5d501302943485217e4c9411a8dfea9d803a14c526ea537b2b2683e5ef8c33660622847cbfd8979433d512",
        "public_key_type": "uncompressed",
        "seed": "357f1c58ca068ebfda512ff1dbc85f19e260e798344c9232",
        "address": "1EV1hewDjJ7YJut2eZ2gruDFcVhRN5qrXq",
        "lot": null,
        "sequence": null
    }
    --------------------------------------------------
    Intermediate Passphrase: passphrasea5kfg7h8ErUgs2xCQtUkFvBqpy32Gge6oVTYVodfJp3jnc39KeJYh2sfadZfAW
    Encrypted WIF: {
        "encrypted_wif": "6PgQLNznFgCPEw9eo1XuKgc2NB5AZYVqbUZRv2UKQdg97aUV7fyoeNwx9s",
        "confirmation_code": "cfrm38V8hYYF3sFQV95Swwovn7x8sP3tjHqcvSskHdpiSMYqCTQ4toR8fggaaPVd22FAK2hXwk8",
        "public_key": "04ef8084a54cf1ee773c7f4bd1808c1b3e916764aed26534966eb44098b4f6b46a44947d626a8f75f982d827711008ce9d1870c07b4db5576a6cabc8a2f20b8f48",
        "seed": "a2cb5b797c5145972961d13f8752aa05e6feca7127cbd318",
        "public_key_type": "uncompressed",
        "address": "16aPsKjLSay9vz7vcoo1TsNUUUwGrCRZDt"
    }
    Confirm Code: {
        "public_key": "04ef8084a54cf1ee773c7f4bd1808c1b3e916764aed26534966eb44098b4f6b46a44947d626a8f75f982d827711008ce9d1870c07b4db5576a6cabc8a2f20b8f48",
        "public_key_type": "uncompressed",
        "address": "16aPsKjLSay9vz7vcoo1TsNUUUwGrCRZDt",
        "lot": 863741,
        "sequence": 1
    }
    BIP38 Decrypted: {
        "wif": "5KVkuuWnSpbTt7WwAvs5hYZm1ETXw5j3NfEh3z6v4iERhD7uJbQ",
        "private_key": "dd5202e63adc9d3362831dcedfa727f066f1499629cd27eb3fa683cabf55a7eb",
        "wif_type": "wif",
        "public_key": "04ef8084a54cf1ee773c7f4bd1808c1b3e916764aed26534966eb44098b4f6b46a44947d626a8f75f982d827711008ce9d1870c07b4db5576a6cabc8a2f20b8f48",
        "public_key_type": "uncompressed",
        "seed": "a2cb5b797c5145972961d13f8752aa05e6feca7127cbd318",
        "address": "16aPsKjLSay9vz7vcoo1TsNUUUwGrCRZDt",
        "lot": 863741,
        "sequence": 1
    }
    --------------------------------------------------
    Intermediate Passphrase: passphraseo12adZTXDqkXn99mNyxdDvT6NfghEcJXTGrcW1sefxfpYsWQmuBg5neozNGByU
    Encrypted WIF: {
        "encrypted_wif": "6PnXPED59kT4A9mnEYGpFBf5BFoYrCfeMrTcjnwLpApGcW4dJatruJGuSY",
        "confirmation_code": "cfrm38VUeVGaevSWvteWmBS6e8AGKUPBkh7n1wYwU7wXdb1Rh1qkbo97WTx9tJWKx4fFS6UBB3y",
        "public_key": "02165a4d1b0da933af4feb58b7d2831aced84cc26e7b7e7213bc6cbcd2f072c6a3",
        "seed": "4f70079f5bdc93a34d7d3caf4313fea5e63d53e3d29063ae",
        "public_key_type": "compressed",
        "address": "1JJ6NEaMazsfq1L9iKCcLepwk21VMy4TQA"
    }
    Confirm Code: {
        "public_key": "02165a4d1b0da933af4feb58b7d2831aced84cc26e7b7e7213bc6cbcd2f072c6a3",
        "public_key_type": "compressed",
        "address": "1JJ6NEaMazsfq1L9iKCcLepwk21VMy4TQA",
        "lot": null,
        "sequence": null
    }
    BIP38 Decrypted: {
        "wif": "L1xgWYbER6FytF3cfVJKaeiXhCm8S3rodEcm5v7LvRQcU8EaRXww",
        "private_key": "8d749fd783d186a3ce9b88871386c1128bcefc4b470e0f95ef537d35429a0b91",
        "wif_type": "wif-compressed",
        "public_key": "02165a4d1b0da933af4feb58b7d2831aced84cc26e7b7e7213bc6cbcd2f072c6a3",
        "public_key_type": "compressed",
        "seed": "4f70079f5bdc93a34d7d3caf4313fea5e63d53e3d29063ae",
        "address": "1JJ6NEaMazsfq1L9iKCcLepwk21VMy4TQA",
        "lot": null,
        "sequence": null
    }
    --------------------------------------------------
    Intermediate Passphrase: passphraseYoVubMghFfXu8JJDfXu6EN1NauvyLWpj8MR6YaBemDfCRbAuzZHAEAG7aPcfKD
    Encrypted WIF: {
        "encrypted_wif": "6PoM8ydznfoqedE1xXTKpQ3bhr8tjT2HRmcZaccCtZxnHbhwZxhBKy5yBe",
        "confirmation_code": "cfrm38VXL6czb2YDRqbDe5AmhV7ZT7JESkvLyYRMAh5NVQ37TUuZrhEa8rEDfSeW96LykTsTizh",
        "public_key": "026a369214f7183ec50964e9d849dbf0b0ea47e6c1eed4c2c89a17d5a4eb36f03b",
        "seed": "c99fd4a4d98d8bd53fd2f298f9446b86792b207aa530576f",
        "public_key_type": "compressed",
        "address": "1CzWDKnZSooKCgSsS4sEtvdfq9MzUQcqgP"
    }
    Confirm Code: {
        "public_key": "026a369214f7183ec50964e9d849dbf0b0ea47e6c1eed4c2c89a17d5a4eb36f03b",
        "public_key_type": "compressed",
        "address": "1CzWDKnZSooKCgSsS4sEtvdfq9MzUQcqgP",
        "lot": 863741,
        "sequence": 1
    }
    BIP38 Decrypted: {
        "wif": "L4Pd4nxLFL86aevLQ1DhETKRNZKxPiFatrS3TuTYE2aD6a44k7KY",
        "private_key": "d5f5f42b3f2d8c69eeb72e1acabe6c3b0c082f1b80ed5be9167368fcb708143f",
        "wif_type": "wif-compressed",
        "public_key": "026a369214f7183ec50964e9d849dbf0b0ea47e6c1eed4c2c89a17d5a4eb36f03b",
        "public_key_type": "compressed",
        "seed": "c99fd4a4d98d8bd53fd2f298f9446b86792b207aa530576f",
        "address": "1CzWDKnZSooKCgSsS4sEtvdfq9MzUQcqgP",
        "lot": 863741,
        "sequence": 1
    }
    --------------------------------------------------
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
    --------------------------------------------------
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
    --------------------------------------------------
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
    --------------------------------------------------
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
    --------------------------------------------------


.. raw:: html

   </details>


Development
===========

We welcome pull requests. To get started, just fork this `github repository <https://github.com/meherett/python-bip38>`_, clone it locally, and run:

::

    pip install -e .[tests,docs] -r requirements.txt


Testing
=======

You can run the tests with:

::

    pytest


Or use **tox** to run the complete suite against the full set of build targets, or pytest to run specific
tests against a specific version of Python.


Contributing
============

Feel free to open an `issue <https://github.com/meherett/python-bip38/issues>`_ if you find a problem,
or a pull request if you've solved an issue. And also any help in testing, development,
documentation and other tasks is highly appreciated and useful to the project.
There are tasks for contributors of all experience levels.

For more information, see the `CONTRIBUTING.md <https://github.com/meherett/python-bip38/blob/master/CONTRIBUTING.md>`_ file.

Donations
=========

Buy me a coffee if You found this tool helpful:

- **BTC** - 12uaGVdX1t86FXLQ4yYPrRQDCK7xGGu82r
- **BTC / ETH / USDT** - `hd.wallet <https://ud.me/hd.wallet>`_

Thank you very much for your support.


License
=======

Distributed under the `MIT <https://github.com/meherett/python-bip38/blob/master/LICENSE>`_ license. See **LICENSE** for more information.

