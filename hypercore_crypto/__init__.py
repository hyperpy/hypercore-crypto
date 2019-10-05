"""hypercore-crypto module."""

from hypercore_crypto.crypto import (  # noqa
    data,
    discovery_key,
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
