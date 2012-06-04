Hookable Object Support
=======================

:mod:`zope.hookable` supports the efficient creation of hookable objects,
which are callable objects that are meant to be replaced by other callables,
at least optionally.

The idea is to create a function that does some default thing and
make it hookable. Later, someone can modify what it does by calling
its sethook method and changing its implementation.  All users of
the function, including those that imported it, will see the
change.

.. doctest::

   >>> from zope.hookable import hookable
   >>> def f41():
   ...     return 41
   >>> f = hookable(f41)
   >>> f.implementation is f.original
   True
   >>> f()
   41

We can replace the implementation, without replacing ``f``:  this means
that modules which have already imported ``f`` will see the hooked version.

.. doctest::

   >>> old = f.sethook(lambda: 42)
   >>> f.implementation is f.original
   False
   >>> old is f41
   True
   >>> f()
   42
   >>> f.original()
   41
   >>> f.implementation()
   42

We can undo the hook by calling ``reset``.

.. doctest::

   >>> f.reset()
   >>> f()
   41
