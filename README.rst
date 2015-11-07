``zope.hookable``
=================

.. image:: https://img.shields.io/pypi/v/zope.hookable.svg
    :target: https://pypi.python.org/pypi/zope.hookable/
    :alt: Latest Version

.. image:: https://travis-ci.org/zopefoundation/zope.hookable.png?branch=master
        :target: https://travis-ci.org/zopefoundation/zope.hookable

.. image:: https://readthedocs.org/projects/zopehookable/badge/?version=latest
        :target: http://zopehookable.readthedocs.org/en/latest/
        :alt: Documentation Status

This package supports the efficient creation of "hookable" objects, which
are callable objects that are meant to be optionally replaced.

The idea is you create a function that does some default thing and make it
hookable. Later, someone can modify what it does by calling its sethook method
and changing its implementation.  All users of the function, including those
that imported it, will see the change.
