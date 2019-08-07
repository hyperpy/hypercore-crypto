"""Cryptography primitives for Hypercore."""

from nacl.bindings import (
    crypto_sign_keypair,
    crypto_sign_PUBLICKEYBYTES,
    crypto_sign_SECRETKEYBYTES,
    crypto_sign_seed_keypair,
)

# https://en.wikipedia.org/wiki/Merkle_tree#Second_preimage_attack
LEAF_TYPE = bytearray([0])
PARENT_TYPE = bytearray([1])
ROOT_TYPE = bytearray([2])
HYPERCORE = bytearray('hypercore', encoding='utf-8')


# TODO(decentral1se): don't forget to type this
def key_pair(seed=None):
    """The signed public/secret key length."""

    public_key = bytearray(crypto_sign_PUBLICKEYBYTES)
    secret_key = bytearray(crypto_sign_SECRETKEYBYTES)

    if seed:
        crypto_sign_seed_keypair(public_key, secret_key, seed)
    else:
        crypto_sign_keypair(public_key, secret_key)

    return {'public-key': public_key, 'secret-key': secret_key}


def sign():
    pass


def verify():
    pass


def data():
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


def blake2b():
    pass
