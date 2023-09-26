Hacking on :mod:`zope.hookable`
================================

Getting the Code
################

The main repository for :mod:`zope.hookable` is in the Zope Foundation
Github repository:

  https://github.com/zopefoundation/zope.hookable

You can get a read-only checkout from there:

.. code-block:: sh

   $ git clone https://github.com/zopefoundation/zope.hookable.git

or fork it and get a writeable checkout of your fork:

.. code-block:: sh

   $ git clone git@github.com/jrandom/zope.hookable.git


Using :mod:`tox`
################

Running Tests on Multiple Python Versions
-----------------------------------------

`tox <http://tox.testrun.org/latest/>`_ is a Python-based test automation
tool designed to run tests against multiple Python versions.  It creates
a ``virtualenv`` for each configured version, installs the current package
and configured dependencies into each ``virtualenv``, and then runs the
configured commands.

:mod:`zope.hookable` configures the following :mod:`tox` environments via
its ``tox.ini`` file:

- The defined Python environments build a ``virtualenv/venv``, install
  :mod:`zope.hookable` and dependencies, and run the tests via
  ``zope.testrunner`` There are environments both for with and without using
  the C code extension.

- The ``coverage`` environment builds a ``virtualenv``,
  installs :mod:`zope.hookable` and dependencies, installs
  :mod:`coverage`, and runs the tests with coverage.

- The ``docs`` environment builds a virtualenv installs :mod:`zope.hookable`
  and dependencies, installs ``Sphinx`` and dependencies, and then builds the
  docs and exercises the doctest snippets.

This example requires that you have a working ``python3.11`` on your path,
as well as an installed ``tox``:

.. code-block:: sh

   $ tox -e py311

Running ``tox`` with no arguments runs all the configured environments,
including building the docs and testing their snippets:

.. code-block:: sh

   $ tox

To run the tests in parallel use:

.. code-block:: sh

   $ tox -p auto

To see the coverage output:

.. code-block:: sh

   $ tox -e coverage

Building the documentation
--------------------------

:mod:`zope.hookable` uses the nifty :mod:`Sphinx` documentation system
for building its docs.

.. code-block:: sh

   $ tox -e docs

It also tests the code snippets in the documentation.

Contributing to :mod:`zope.hookable`
####################################

Submitting a Bug Report
-----------------------

:mod:`zope.hookable` tracks its bugs on Github:


  https://github.com/zopefoundation/zope.hookable/issues

Please submit bug reports and feature requests there.


Sharing Your Changes
--------------------

If have made a change you would like to share, the best route is to fork
the GitHub repository, check out your fork, make your changes on a branch
in your fork, and push it.  You can then submit a pull request from your
branch:

  https://github.com/zopefoundation/zope.hookable/pulls
