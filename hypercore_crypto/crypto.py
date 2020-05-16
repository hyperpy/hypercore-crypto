"""Cryptography primitives for Hypercore."""

from hashlib import blake2b
from typing import Optional, Sequence, Tuple

from merkle_tree_stream import MerkleTreeNode
from pysodium import (
    crypto_generichash,
    crypto_generichash_BYTES,
    crypto_sign_detached,
    crypto_sign_keypair,
    crypto_sign_seed_keypair,
    crypto_sign_SEEDBYTES,
    crypto_sign_verify_detached,
    randombytes,
)

__all__ = [
    "key_pair",
    "sign",
    "verify",
    "data",
    "leaf",
    "parent",
    "tree",
    "random_bytes",
    "discovery_key",
]

# https://en.wikipedia.org/wiki/Merkle_tree#Second_preimage_attack
LEAF_TYPE = bytes([0])
PARENT_TYPE = bytes([1])
ROOT_TYPE = bytes([2])
HYPERCORE = bytes("hypercore", encoding="utf-8")


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


def data(data: bytes) -> bytes:
    """The hashed digest of data input.

    :param data: The data to be hashed
    """
    return _blake2bify([LEAF_TYPE, _to_unsigned_64_int(len(data)), data])


def leaf(leaf: MerkleTreeNode) -> bytes:
    """The hashed digest of the leaf.

    :param leaf: The leaf data to be hashed
    """
    return data(leaf.data)


def parent(child: MerkleTreeNode, parent: MerkleTreeNode) -> bytes:
    if child.index > parent.index:
        raise ValueError("Child index is greater than parent?")

    values = [
        PARENT_TYPE,
        _to_unsigned_64_int(child.size + parent.size),
        child.hash,
        parent.hash,
    ]

    return _blake2bify(values)


def tree(roots: Sequence[MerkleTreeNode]) -> bytes:
    """Hashed tree roots.

    :param roots: A list of root nodes
    """
    to_be_hashed = []
    to_be_hashed.append(ROOT_TYPE)

    for root in roots:
        to_be_hashed.append(root.hash)
        to_be_hashed.append(root.index)
        to_be_hashed.append(root.size)

    return _blake2bify(to_be_hashed)


def random_bytes(size: int) -> bytes:
    """Random bytes with specified length.

    :param size The length of the random bytes
    """
    return randombytes(size)


def discovery_key(public_key: bytes) -> bytes:
    """The discovery key for a tree.

    :param public_key: The public key for hashing
    """
    return crypto_generichash(HYPERCORE, k=public_key)


def _to_unsigned_64_int(num: int) -> bytes:
    """Convert an integer to unsigned 64 bit bytes.

    See https://stackoverflow.com/a/45434265.

    :param num: The integer to be converted
    """
    return int(num).to_bytes(8, byteorder="big", signed=False)


def _blake2bify(data: Sequence[bytes]) -> bytes:
    """Hashed bytes from the Blake2b hash function.

    :param data: A list of byte values to be hashed
    """
    hash_func = blake2b(digest_size=crypto_generichash_BYTES)

    for _data in data:
        hash_func.update(_data)

    return hash_func.digest()
