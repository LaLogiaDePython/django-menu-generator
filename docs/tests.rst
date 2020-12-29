Running the tests
==================

To run the tests against configured environments:

* Install pyenv and add all of the supported python versions there
* Add all of the version to your locals `pyenv local system 3.7.9 3.6.12 3.5.10` for example
* Install the development dependencies in `requirements_dev.txt`
* Run the tests with tox

::

    tox
