Get started
-----------

Install `Tox`_ with:

.. _tox: http://tox.readthedocs.io/

.. code-block:: bash

    $ pip install --user tox

Run tests
---------

.. code-block:: bash

    tox -e py37

Lint source
-----------

.. code-block:: bash

    tox -e lint

Format source
-------------

.. code-block:: bash

    tox -e format

Type check source
-----------------

.. code-block:: bash

    tox -e type

Release Process
---------------

.. code-block:: bash

    $ tox -e release
