Get started
-----------

Install `Tox`_ with:

.. _tox: http://tox.readthedocs.io/

.. code-block:: bash

    $ pip install --user tox

Run tests
---------

.. code-block:: bash

    tox -e test

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

Add a change entry and re-generate the changelog:

.. code-block:: bash

    $ towncrier

Make a new release tag:

.. code-block:: bash

    $ git tag x.x.x
    $ git push --tags

If you have a development install locally, you can verify:

.. code-block:: bash

    $ hypercore-crypto --version

Then run the release process:

.. code-block:: bash

    $ tox -e metadata-release
    $ tox -e release
