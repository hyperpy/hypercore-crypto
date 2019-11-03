Get started
-----------

Install `Tox`_.

.. _tox: http://tox.readthedocs.io/

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

Build the documentation
-----------------------

.. code-block:: bash

    $ tox -e docs
    $ tox -e docs-livereload

Make a new release
------------------

Ensure metadata for packaging is correct.

.. code-block:: bash

    $ tox -e metadata-release

Generate the changelog with the next target version.

.. code-block:: bash

    $ export VERSION=1.0.1 tox -e changelog

Make a new Git tag.

.. code-block:: bash

    $ git tag  -a 1.0.1

And finally, make a new release.

.. code-block:: bash

    $ tox -e release
