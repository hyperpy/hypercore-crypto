"""hypercore-crypto module."""

# Note(decentral1se): Included to match export list of the original Javascript
# reference implementation. However, we don't implement this function
# ourselves.
from nacl.hash import blake2b  # noqa

from hypercore_crypto.crypto import (  # noqa
    blake2b,
    data,
    discovery_key,
    encode_unsigned_int64,
    key_pair,
    leaf,
    parent,
    random_bytes,
    sign,
    tree,
    verify,
)

try:
    import pkg_resources
except ImportError:
    pass


try:
    __version__ = pkg_resources.get_distribution('hypercore_crypto').version
except Exception:
    __version__ = 'unknown'
