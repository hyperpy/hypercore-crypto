"""Cryptography primitives for Hypercore."""

from typing import Optional, Tuple

from pysodium import (
    crypto_sign_detached,
    crypto_sign_keypair,
    crypto_sign_seed_keypair,
    crypto_sign_SEEDBYTES,
    crypto_sign_verify_detached,
)

# https://en.wikipedia.org/wiki/Merkle_tree#Second_preimage_attack
LEAF_TYPE = bytearray([0])
PARENT_TYPE = bytearray([1])
ROOT_TYPE = bytearray([2])
HYPERCORE = bytearray('hypercore', encoding='utf-8')


def key_pair(seed: Optional[bytes] = None) -> Tuple[bytes, bytes]:
    """A new public key and secret key pair.

    :param seed: Seed value. Must be at least 32 characters in length
    """
    if seed:
        if len(seed) < crypto_sign_SEEDBYTES:
            message = "'seed' argument must be of length > {}"
            raise ValueError(message.format(crypto_sign_SEEDBYTES))
        return crypto_sign_seed_keypair(seed)
    return crypto_sign_keypair()


def sign(message: bytes, secret_key: bytes) -> bytes:
    """A message signature.

    :param message: The message to be signed
    :param secret_key: The secret key to use during signing
    """
    return crypto_sign_detached(message, secret_key)


def verify(message: bytes, signature: bytes, public_key: bytes) -> bool:
    """Verify an unsigned message with accompanying signature.

    :param message: The unsigned message to verify
    :param signature: The signature to be verified
    :param public_key: The public key to use during verifying
    """
    try:
        crypto_sign_verify_detached(signature, message, public_key)
    except ValueError:
        return False
    return True


def data(data: bytes):
    pass


def leaf():
    pass


def parent():
    pass


def tree():
    pass


def random_bytes():
    pass


def discovery_key():
    pass
