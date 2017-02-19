===========
Otter Pilot
===========

Need a buddy on the terminal? I'm your buddy! Give me all your scripts and
together, we can make our lives easier.

Installing
----------

.. code-block:: bash

    pip install .

Running
-------

.. code-block:: bash

   otter --help

Creating A New Copilot
----------------------

.. code-block:: bash

    otter-pilot-sample
    ├── setup.py
    └── src
        └── otter
            ├── commands
            │   ├── __init__.py
            │   └── sample.py
            └── __init__.py

    3 directories, 4 files

`setup.py`
^^^^^^^^^^

.. code-block:: python

    #!/usr/bin/env python3
    from setuptools import find_packages, setup

    setup(
        name='otter-pilot-sample',
        namespace_packages=['otter'],
        package_dir={'': 'src'},
        packages=find_packages(where='src'), )

`src/otter/__init__.py`
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    __import__('pkg_resources').declare_namespace(__name__)

`src/otter/commands/sample.py`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    """Sample otter pilot."""
    import click


    @click.command()
    def main():
        """Required main."""
        print('Sample command.')
