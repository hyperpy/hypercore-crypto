"""Cryptography primitives test module."""

import pytest
from merkle_tree_stream import MerkleTreeNode
from pysodium import crypto_sign_PUBLICKEYBYTES, crypto_sign_SECRETKEYBYTES

from hypercore_crypto import (
    data,
    discovery_key,
    key_pair,
    parent,
    random_bytes,
    sign,
    verify,
)


def test_key_pair_seed_length():
    with pytest.raises(ValueError) as exception:
        key_pair(b"world hello")
        assert "must be of length" in str(exception)


def test_key_pair_length():
    public_key, secret_key = key_pair()
    assert len(public_key) == crypto_sign_PUBLICKEYBYTES
    assert len(secret_key) == crypto_sign_SECRETKEYBYTES


def test_sign():
    message = b"hello world"
    _, secret_key = key_pair()
    signature = sign(message, secret_key)
    assert message not in signature
    assert len(signature) == 64


def test_verify():
    message = b"hello world"
    public_key, secret_key = key_pair()
    signature = sign(message, secret_key)
    assert verify(message, signature, public_key)


def test_data_digest():
    assert (
        data(b"hello world").hex()
        == "ccfa4259ee7c41e411e5770973a49c5ceffb5272d6a37f2c6f2dac2190f7e2b7"
    )


def test_random_bytes():
    assert len(random_bytes(32)) == 32


def test_parent_digest():
    _data = b"hello world"
    _parent = parent(
        MerkleTreeNode(
            index=0, size=11, hash=data(_data), parent=None, data=None
        ),
        MerkleTreeNode(
            index=2, size=11, hash=data(_data), parent=None, data=None
        ),
    )
    assert (
        _parent.hex()
        == "43563406adba8b34b133fdca32d0a458c5be769615e01df30e6535ccd3c075f0"
    )


def test_discovery_key_generated():
    assert discovery_key(random_bytes(32)) is not None
