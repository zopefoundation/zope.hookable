===============
 zope.hookable
===============

.. image:: https://img.shields.io/pypi/v/zope.hookable.svg
        :target: https://pypi.python.org/pypi/zope.hookable/
        :alt: Latest release

.. image:: https://img.shields.io/pypi/pyversions/zope.hookable.svg
        :target: https://pypi.org/project/zope.hookable/
        :alt: Supported Python versions

.. image:: https://github.com/zopefoundation/zope.hookable/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/zopefoundation/zope.hookable/actions/workflows/tests.yml

.. image:: https://readthedocs.org/projects/zopehookable/badge/?version=latest
        :target: https://zopehookable.readthedocs.io/en/latest/
        :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/zopefoundation/zope.hookable/badge.svg?branch=master
        :target: https://coveralls.io/github/zopefoundation/zope.hookable?branch=master


This package supports the efficient creation of "hookable" objects, which
are callable objects that are meant to be optionally replaced.

The idea is that you create a function that does some default thing and make it
hookable. Later, someone can modify what it does by calling its sethook method
and changing its implementation.  All users of the function, including those
that imported it, will see the change.

Documentation is hosted at https://zopehookable.readthedocs.io
