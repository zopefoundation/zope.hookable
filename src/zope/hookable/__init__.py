##############################################################################
#
# Copyright (c) 2003 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Hookable object support
"""
import os
import platform


# Keep these two flags separate:  we want the `_PURE_PYTHON` one
# to represent that the flag is explicitly set to '1' in the environment,
# since our 'tox.ini' sets it to '0' for its environments which expect
# to test the C extension.
_PYPY_OR_JAVA = platform.python_implementation() in ('PyPy', 'Jython')
_PURE_PYTHON = os.environ.get('PURE_PYTHON') == '1'


class _py_hookable:
    __slots__ = ('_original', '_implementation')

    def __init__(self, *args, **kw):
        if not args and 'implementation' in kw:
            args = (kw.pop('implementation'),)
        if kw:
            raise TypeError('Unknown keyword arguments')
        if len(args) != 1:
            raise TypeError('Exactly one argument required')
        self._original = self._implementation = args[0]

    @property
    def original(self):
        return self._original

    @property
    def implementation(self):
        return self._implementation

    @property
    def __doc__(self):
        return self._original.__doc__

    @property
    def __dict__(self):
        return getattr(self._original, '__dict__', {})

    @property
    def __bases__(self):
        return getattr(self._original, '__bases__', ())

    def sethook(self, new_callable):
        old, self._implementation = self._implementation, new_callable
        return old

    def reset(self):
        self._implementation = self._original

    def __call__(self, *args, **kw):
        return self._implementation(*args, **kw)


try:
    from zope.hookable._zope_hookable import hookable as _c_hookable
except ModuleNotFoundError:  # pragma: no cover
    _c_hookable = None

if _PYPY_OR_JAVA or _PURE_PYTHON or _c_hookable is None:
    hookable = _py_hookable
else:  # pragma: no cover
    hookable = _c_hookable
