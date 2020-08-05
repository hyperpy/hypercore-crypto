# hypercore-crypto

[![Build Status](https://drone.autonomic.zone/api/badges/hyperpy/hypercore-crypto/status.svg)](https://drone.autonomic.zone/hyperpy/hypercore-crypto)

## Cryptography primitives for Hypercore

## Install

```sh
$ pip install hypercore-crypto
```

## Example

```python
from pysodium import crypto_sign_PUBLICKEYBYTES

from hypercore_crypto import data, key_pair

public_key, secret_key = key_pair()
assert len(public_key) == crypto_sign_PUBLICKEYBYTES

print(data(b"hello world").hex())
```

Output:

```sh
ccfa4259ee7c41e411e5770973a49c5ceffb5272d6a37f2c6f2dac2190f7e2b7
```
