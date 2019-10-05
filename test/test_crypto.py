"""Cryptography primitives test module."""

import pytest

from hypercore_crypto import key_pair, sign, verify
from pysodium import crypto_sign_PUBLICKEYBYTES, crypto_sign_SECRETKEYBYTES


def test_key_pair_seed_length():
    with pytest.raises(ValueError) as exception:
        key_pair(b'wrong')
        assert 'must be of length' in str(exception)


def test_key_pair_length():
    public_key, secret_key = key_pair()
    assert len(public_key) == crypto_sign_PUBLICKEYBYTES
    assert len(secret_key) == crypto_sign_SECRETKEYBYTES


def test_sign():
    message = b'mymessage'
    _, secret_key = key_pair()
    assert message not in sign(message, secret_key)


def test_verify():
    message = b'mymessage'
    public_key, secret_key = key_pair()
    signature = sign(message, secret_key)
    assert verify(message, signature, public_key)
