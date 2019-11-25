.. _example:

*******
Example
*******

.. code-block:: python

    from hypercore_crypto import key_pair, sign, verify

    public_key, secret_key = key_pair()
    signature = sign(b'hello world', secret_key)
    verify(message, signature, public_key)
