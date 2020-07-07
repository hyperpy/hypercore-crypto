# hypercore-crypto

[![Build Status](https://drone.autonomic.zone/api/badges/hyperpy/hypercore-crypto/status.svg)](https://drone.autonomic.zone/hyperpy/hypercore-crypto)

## Cryptography primitives for Hypercore

## Install

```sh
$ pip install hypercore-crypto
```

## Example

```python
from hypercore_crypto import data, key_pair
from pysodium import crypto_sign_PUBLICKEYBYTES

public_key, secret_key = key_pair()
assert len(public_key) == crypto_sign_PUBLICKEYBYTES
print(data(b"hello world").hex())
```
