"""Cryptography primitives for Hypercore."""

from typing import Optional, Tuple

import nacl.exceptions
from nacl.bindings import (
    crypto_sign,
    crypto_sign_keypair,
    crypto_sign_seed_keypair,
)
from nacl.hash import blake2b
from nacl.signing import VerifyKey

# https://en.wikipedia.org/wiki/Merkle_tree#Second_preimage_attack
LEAF_TYPE = bytearray([0])
PARENT_TYPE = bytearray([1])
ROOT_TYPE = bytearray([2])
HYPERCORE = bytearray('hypercore', encoding='utf-8')


def key_pair(seed: Optional[bytes] = None) -> Tuple[bytes, bytes]:
    """A new public key and secret key pair.

    The seed must be at least 32 characters in length.
    """
    if seed:
        return crypto_sign_seed_keypair(seed)
    return crypto_sign_keypair()


def sign(message: bytes, secret_key: bytes) -> bytes:
    """Signed message from a secret key."""
    return crypto_sign(message, secret_key)


def verify(signed_message: bytes, signature: bytes, public_key: bytes) -> bool:
    """Verify a signed message."""
    try:
        VerifyKey(public_key).verify(signed_message, signature=signature)
    except (nacl.exceptions.TypeError, nacl.exceptions.BadSignatureError):
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


def encode_unsigned_int64():
    pass
