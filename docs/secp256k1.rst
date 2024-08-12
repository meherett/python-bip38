:orphan:

=========
Secp256k1
=========

The `Secp256k1` module provides classes that encapsulate the elliptic curve operations used in cryptographic applications, particularly for Bitcoin and other cryptocurrencies. It includes classes for working with points on the curve, public keys, and private keys.

.. autoclass:: bip38.secp256k1.point.Point
   :members:

   The `Point` class represents a point on the Secp256k1 elliptic curve. This class provides methods for point arithmetic, such as addition and multiplication, essential for cryptographic operations.

.. autoclass:: bip38.secp256k1.public_key.PublicKey
   :members:

   The `PublicKey` class encapsulates a public key derived from the Secp256k1 curve. It includes methods for generating and validating public keys, as well as performing key operations like verification of signatures.

.. autoclass:: bip38.secp256k1.private_key.PrivateKey
   :members:

   The `PrivateKey` class represents a private key associated with the Secp256k1 curve. This class provides methods for key generation, signing messages, and deriving the corresponding public key.
