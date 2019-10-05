"""Cryptography primitives test module."""

from hypercore_crypto import key_pair


def test_key_pair_length():
    public_key, secret_key = key_pair()
    assert len(public_key) == 32
    assert len(secret_key) == 64
