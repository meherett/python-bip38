===========================================
Bitcoin Improvement Proposal - 0038 / BIP38
===========================================

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

Python library for implementation of Bitcoin Improvement Proposal - 0038 / BIP38 protocol. It supports both `No EC-multiply <https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki#encryption-when-ec-multiply-flag-is-not-used>`_ and `EC-multiply <https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki#encryption-when-ec-multiply-mode-is-used>`_ modes.

BIP38 is a cryptographic standard that defines a method for encrypting and securing private keys associated with Bitcoin addresses. It provides a way to create encrypted versions of private keys, which can then be decrypted using a passphrase. This adds an additional layer of security to the process of storing and transmitting private keys.

By encrypting a private key with BIP38, users can protect their funds even if the encrypted private key is exposed. This is because an attacker would need to know the passphrase in order to decrypt the private key and gain access to the associated funds. BIP38 encryption is often used to create "paper wallets" or physical copies of Bitcoin private keys that can be stored offline for enhanced security.

For more info see the `Passphrase-protected private key - BIP38 <https://en.bitcoin.it/wiki/BIP_0038>`_ specs.

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

no EC multiply:
_______________

::

    #!/usr/bin/env python3

    from bip38 import (
        private_key_to_wif, bip38_encrypt, bip38_decrypt
    )
    from typing import List

    import json

    # Private key
    PRIVATE_KEY: str = "cbf4b9f70470856bb4f40f80b87edb90865997ffee6df315ab166d713af433a5"
    # Passphrase / password
    PASSPHRASE: str = "meherett"  # u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
    # To show detail
    DETAIL: bool = True
    # Wallet important format's
    WIFs: List[str] = [
        private_key_to_wif(private_key=PRIVATE_KEY, wif_type="wif"),  # No compression
        private_key_to_wif(private_key=PRIVATE_KEY, wif_type="wif-compressed")  # Compression
    ]

    for WIF in WIFs:

        print("WFI:", WIF)
        encrypted_wif: str = bip38_encrypt(
            wif=WIF, passphrase=PASSPHRASE
        )
        print("BIP38 Encrypted WIF:", encrypted_wif)
        print("BIP38 Decrypted:", json.dumps(bip38_decrypt(
            encrypted_wif=encrypted_wif, passphrase=PASSPHRASE, detail=DETAIL
        ), indent=4))

        print("-" * 125)


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

.. raw:: html

   </details>


EC multiply:
------------

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
    SAMPLES: List[dict] = [
        # Random owner salt & seed, No compression, No lot & sequence
        {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "uncompressed", "lot": None, "sequence": None},
        # Random owner salt & seed, No compression, With lot & sequence
        {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "uncompressed", "lot": 863741, "sequence": 1},
        # Random owner salt & seed, Compression, No lot & sequence
        {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "compressed", "lot": None, "sequence": None},
        # Random owner salt & seed, Compression, With lot & sequence
        {"owner_salt": os.urandom(8), "seed": os.urandom(24), "public_key_type": "compressed", "lot": 863741, "sequence": 1},
        # With owner salt & seed, No compression, No lot & sequence
        {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "uncompressed", "lot": None, "sequence": None},
        # With owner salt & seed, No compression, With lot & sequence
        {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "uncompressed", "lot": 567885, "sequence": 1},
        # With owner salt & seed, Compression, No lot & sequence
        {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "compressed", "lot": None, "sequence": None},
        # With owner salt & seed, Compression, With lot & sequence
        {"owner_salt": "75ed1cdeb254cb38", "seed": "99241d58245c883896f80843d2846672d7312e6195ca1a6c", "public_key_type": "compressed", "lot": 369861, "sequence": 1},
    ]

    for SAMPLE in SAMPLES:

        intermediate_passphrase: str = intermediate_code(
            passphrase=PASSPHRASE, owner_salt=SAMPLE["owner_salt"], lot=SAMPLE["lot"], sequence=SAMPLE["sequence"]
        )

        print("Intermediate Passphrase:", intermediate_passphrase)

        encrypted_wif: dict = create_new_encrypted_wif(
            intermediate_passphrase=intermediate_passphrase, public_key_type=SAMPLE["public_key_type"], seed=SAMPLE["seed"]
        )
        print("Encrypted WIF:", json.dumps(encrypted_wif, indent=4))

        print("Confirm Code:", json.dumps(confirm_code(
            passphrase=PASSPHRASE, confirmation_code=encrypted_wif["confirmation_code"], detail=DETAIL
        ), indent=4))

        print("BIP38 Decrypted:", json.dumps(bip38_decrypt(
            encrypted_wif=encrypted_wif["encrypted_wif"], passphrase=PASSPHRASE, detail=DETAIL
        ), indent=4))

        print("-" * 125)

.. raw:: html

   <details>
        <summary>Output</summary>

.. code-block:: shell

    Intermediate Passphrase: passphraseqtFiMLZSKYBJo6ZdivCqkPyMX3bnPFnedQRtEHWHmADXqEfSyJHE1CLuTbF6Wf
    Encrypted WIF: {
        "encrypted_wif": "6PfPd3hFPNjBMqirrvSSgEtDnErh9BzqK1NUdk6fiQCaN7LwdGFus4PhQV",
        "confirmation_code": "cfrm38V5QE7EN2eF9SfWsesQCjJZSoSjc5YiqLDCgEJoqEDoV2D9f7NRXSqQHsWb3MKogaN8zAs",
        "public_key": "0412bb1ec0a2fa1e7c90f4061578d8deeaa6984c9ec5c37717546fb0d127573a03f3050a9f7cb24f62e107c43470388531193fcd8b878618cf74e1d71698069e07",
        "seed": "d010fe7f60a25982f3ee7e056e1bcd027f1c15bd26ddd221",
        "public_key_type": "uncompressed",
        "address": "1CHsGDzDbZJPVKiC9hUKe1hnAevwu5RTKi"
    }
    Confirm Code: {
        "public_key": "0412bb1ec0a2fa1e7c90f4061578d8deeaa6984c9ec5c37717546fb0d127573a03f3050a9f7cb24f62e107c43470388531193fcd8b878618cf74e1d71698069e07",
        "public_key_type": "uncompressed",
        "address": "1CHsGDzDbZJPVKiC9hUKe1hnAevwu5RTKi",
        "lot": null,
        "sequence": null
    }
    BIP38 Decrypted: {
        "wif": "5Jp53JGVEkX2dxXXJyb2UdJw3259yk3YjJCdhcHA3eXpJsr6PBB",
        "private_key": "83348354ac6638ad7ea78505bd85ff96485e17edcffe85572df9a66f997e1324",
        "wif_type": "wif",
        "public_key": "0412bb1ec0a2fa1e7c90f4061578d8deeaa6984c9ec5c37717546fb0d127573a03f3050a9f7cb24f62e107c43470388531193fcd8b878618cf74e1d71698069e07",
        "public_key_type": "uncompressed",
        "seed": "d010fe7f60a25982f3ee7e056e1bcd027f1c15bd26ddd221",
        "address": "1CHsGDzDbZJPVKiC9hUKe1hnAevwu5RTKi",
        "lot": null,
        "sequence": null
    }
    -----------------------------------------------------------------------------------------------------------------------------
    Intermediate Passphrase: passphrasedcXyya37d7imwPshCWV77N6SdDCXCGkbUDQ8dgg39Xutzej2UoNTRXCWjcVSk3
    Encrypted WIF: {
        "encrypted_wif": "6PgHqxpPU2tA4rqjL5gMMkqeahFRRDDe3g1jJy5mhQdNasT1WtwEkzGcdk",
        "confirmation_code": "cfrm38V8LPy6dJTRpd7Qs74zLAdE26F3ZGqJ1Dmr5HheKY2miBwbJMdk1qY6VhZDjNJkitu5Di5",
        "public_key": "049b3dcf56a38df3a2437055f2ad3aec950a54f7205bbcc9949d5299ee4e0215d0924a756dce3baf3356da8465341ebf1c580c4ee13e2602508df57ec49a15e981",
        "seed": "8195ac15d84c139531faec482a9d312f86f79242acb728a7",
        "public_key_type": "uncompressed",
        "address": "17YeFTwCoxVhz5P8KiGHv4d8JwUEwPUbhj"
    }
    Confirm Code: {
        "public_key": "049b3dcf56a38df3a2437055f2ad3aec950a54f7205bbcc9949d5299ee4e0215d0924a756dce3baf3356da8465341ebf1c580c4ee13e2602508df57ec49a15e981",
        "public_key_type": "uncompressed",
        "address": "17YeFTwCoxVhz5P8KiGHv4d8JwUEwPUbhj",
        "lot": 863741,
        "sequence": 1
    }
    BIP38 Decrypted: {
        "wif": "5KGpex1ZJaPoG2L6cHtzAU1nM9un8nw3uD8d6v8xGJs6M6q9qQj",
        "private_key": "bff2e24adfd0323ecd0b969cb3768adba578a0ea503306fd647e6b11e8739d70",
        "wif_type": "wif",
        "public_key": "049b3dcf56a38df3a2437055f2ad3aec950a54f7205bbcc9949d5299ee4e0215d0924a756dce3baf3356da8465341ebf1c580c4ee13e2602508df57ec49a15e981",
        "public_key_type": "uncompressed",
        "seed": "8195ac15d84c139531faec482a9d312f86f79242acb728a7",
        "address": "17YeFTwCoxVhz5P8KiGHv4d8JwUEwPUbhj",
        "lot": 863741,
        "sequence": 1
    }
    -----------------------------------------------------------------------------------------------------------------------------
    Intermediate Passphrase: passphraseoH4GEqnBR53ipb9gwLfbJM8nKMx4LnZPCzYbvgPyR2zYkF5DqKrW2gf8DZ8s7y
    Encrypted WIF: {
        "encrypted_wif": "6PnYW3V9jp8sKA4aMEWJjBvNTRtVYBCSRWb6Yja6xZqBhVVrDXWSnYz2at",
        "confirmation_code": "cfrm38VUi8UMcgVUDQRSjjn1VxVLfHYQxphSRvAQYSU244oNwHoxt24UByEnUeqSbN6QatRVtaR",
        "public_key": "022604144840ed73bc5055916e2e114efe2a706ee71033b48644e3e322a2c58dab",
        "seed": "e0051112f4903c0bbe52dc698c031467bf4646040b6b12a3",
        "public_key_type": "compressed",
        "address": "1EVSAfcUHG8Ce2CF74QwW58wSr7WY4QBaH"
    }
    Confirm Code: {
        "public_key": "022604144840ed73bc5055916e2e114efe2a706ee71033b48644e3e322a2c58dab",
        "public_key_type": "compressed",
        "address": "1EVSAfcUHG8Ce2CF74QwW58wSr7WY4QBaH",
        "lot": null,
        "sequence": null
    }
    BIP38 Decrypted: {
        "wif": "Kz2v4F99WaPamvCC2LwGTwdr25TnUXUB991wKpVhHGxtJE6iAveq",
        "private_key": "53f56bb7fc1a9e9682aa55be6e501776fc9ac2369654c6c85b00b87d41ab8229",
        "wif_type": "wif-compressed",
        "public_key": "022604144840ed73bc5055916e2e114efe2a706ee71033b48644e3e322a2c58dab",
        "public_key_type": "compressed",
        "seed": "e0051112f4903c0bbe52dc698c031467bf4646040b6b12a3",
        "address": "1EVSAfcUHG8Ce2CF74QwW58wSr7WY4QBaH",
        "lot": null,
        "sequence": null
    }
    -----------------------------------------------------------------------------------------------------------------------------
    Intermediate Passphrase: passphraseaWdkWraG6G7W9TCAhCtmoLXbFWdDYjrG8gtv2VPCY7mCvJgbFCoktRKm4ePsQU
    Encrypted WIF: {
        "encrypted_wif": "6PoHWWXXJTibxUGKcVmyts86N8rcTHXJpAoj5VeRf2FhJqj2oQgCsHheKg",
        "confirmation_code": "cfrm38VX8GoZrei4jxLQKA6Mx2zSWkrQZPhxQW1FcCRjtizmQDoWoomm5SW63ESEAUuLkA8MFmc",
        "public_key": "025f4476d9d8c093a04499fe9d7fbd34533dae14a498a2506a90d6cfdda66e99b3",
        "seed": "1ac2513b9149124a0a0d697ae76cbb4583e85d4a652330a6",
        "public_key_type": "compressed",
        "address": "1ESHxrqxMLrdzwfif9nQbq4PTGhDGi1uq2"
    }
    Confirm Code: {
        "public_key": "025f4476d9d8c093a04499fe9d7fbd34533dae14a498a2506a90d6cfdda66e99b3",
        "public_key_type": "compressed",
        "address": "1ESHxrqxMLrdzwfif9nQbq4PTGhDGi1uq2",
        "lot": 863741,
        "sequence": 1
    }
    BIP38 Decrypted: {
        "wif": "L2otjF2N8EpKvh541jw1n3MrXZLpnCfQ2GB4eiGZLFwoSj1UHprw",
        "private_key": "a6c57a43bf2a8ecc153b6b1e8807ec2409033616d4fc98a4edae277c02312eb7",
        "wif_type": "wif-compressed",
        "public_key": "025f4476d9d8c093a04499fe9d7fbd34533dae14a498a2506a90d6cfdda66e99b3",
        "public_key_type": "compressed",
        "seed": "1ac2513b9149124a0a0d697ae76cbb4583e85d4a652330a6",
        "address": "1ESHxrqxMLrdzwfif9nQbq4PTGhDGi1uq2",
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

