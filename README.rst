.. _header:

****************
hypercore-crypto
****************

.. image:: https://img.shields.io/badge/license-GPL-brightgreen.svg
   :target: LICENSE
   :alt: Repository license

.. image:: https://badge.fury.io/py/hypercore-crypto.svg
   :target: https://badge.fury.io/py/hypercore-crypto
   :alt: PyPI package

.. image:: https://travis-ci.com/datpy/hypercore-crypto.svg?branch=master
   :target: https://travis-ci.com/datpy/hypercore-crypto
   :alt: Travis CI result

.. image:: https://readthedocs.org/projects/hypercore-crypto/badge/?version=latest
   :target: https://hypercore-crypto.readthedocs.io/en/latest/
   :alt: Documentation status

.. image:: https://img.shields.io/badge/support-maintainers-brightgreen.svg
   :target: https://decentral1.se
   :alt: Support badge

.. _introduction:

Cryptography primitives for Hypercore
-------------------------------------

Cryptography primitives for `Hypercore`_ (WIP).

.. _Hypercore: https://hypercore.readthedocs.io

.. _example:

Example
*******

.. code-block:: python

    from hypercore_crypto import key_pair, sign, verify

    public_key, secret_key = key_pair()
    signature = sign(b'hello world', secret_key)
    verify(message, signature, public_key)

.. _documentation:

Documentation
*************

* `hypercore-crypto.readthedocs.io`_

.. _hypercore-crypto.readthedocs.io: https://hypercore-crypto.readthedocs.io/

Mirroring
*********

* `hack.decentral1.se/datpy/hypercore-crypto`_
* `github.com/datpy/hypercore-crypto`_

.. _hack.decentral1.se/datpy/hypercore-crypto: https://hack.decentral1.se/datpy/hypercore-crypto
.. _github.com/datpy/hypercore-crypto: https://github.com/datpy/hypercore-crypto
