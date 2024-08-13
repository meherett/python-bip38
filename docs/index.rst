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

    pip install git+git://github.com/meherett/python-bip38.git


For the versions available, see the `tags on this repository <https://github.com/meherett/python-bip38/tags>`_.

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
    PASSPHRASE: str = "meherett"  # u"\u03D2\u0301\u0000\U00010400\U0001F4A9"
    # Network type
    NETWORK:str = "mainnet"
    # To show detail
    DETAIL: bool = True
    # Initialize BIP38 instance
    bip38: BIP38 = BIP38(
        cryptocurrency=Cryptocurrency, network=NETWORK
    )
    # Wallet Important Format's
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

    for kwarg in KWARGS:

        intermediate_passphrase: str = bip38.intermediate_code(
            passphrase=PASSPHRASE, owner_salt=kwarg["owner_salt"], lot=kwarg["lot"], sequence=kwarg["sequence"]
        )
        print("Intermediate Passphrase:", intermediate_passphrase)

        encrypted_wif: dict = bip38.create_new_encrypted_wif(
            intermediate_passphrase=intermediate_passphrase, public_key_type=kwarg["public_key_type"], seed=kwarg["seed"],
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

.. raw:: html

   </details>


Development
===========

We welcome pull requests. To get started, just fork this `github repository <https://github.com/meherett/python-bip38>`_, clone it locally, and run:

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

Feel free to open an `issue <https://github.com/meherett/python-bip38/issues>`_ if you find a problem,
or a pull request if you've solved an issue. And also any help in testing, development,
documentation and other tasks is highly appreciated and useful to the project.
There are tasks for contributors of all experience levels.

For more information, see the `CONTRIBUTING.md <https://github.com/meherett/python-bip38/blob/master/CONTRIBUTING.md>`_ file.

Donations
=========

Buy me a coffee if You found this tool helpful:

- **Bitcoin** - 12uaGVdX1t86FXLQ4yYPrRQDCK7xGGu82r
- **Ethereum / Tether** - 0xCCAad7A87fd81553d0F93F743Fb4Fc6B213b228B
- **Bitcoin / Ethereum / Tether** - With Unstoppable `hd.wallet <https://ud.me/hd.wallet>`_

Thank you very much for your support.


License
=======

Distributed under the `MIT <https://github.com/meherett/python-bip38/blob/master/LICENSE>`_ license. See **LICENSE** for more information.
