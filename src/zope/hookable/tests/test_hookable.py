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
"""Test the hookable support Extension
"""
import unittest

def return_foo():
    return 'FOO'

def return_bar():
    return 'BAR'

def not_called():
    raise AssertionError("This should not be called")

class PyHookableTests(unittest.TestCase):

    def _callFUT(self, *args, **kw):
        from zope.hookable import _py_hookable
        return _py_hookable(*args, **kw)

    def test_before_hook(self):
        hooked = self._callFUT(return_foo)
        self.assertIs(hooked.original, return_foo)
        self.assertIs(hooked.implementation, return_foo)
        self.assertEqual(hooked(), 'FOO')

    def test_after_hook(self):
        hooked = self._callFUT(not_called)
        old = hooked.sethook(return_bar)
        self.assertIs(old, not_called)
        self.assertIs(hooked.original, not_called)
        self.assertIs(hooked.implementation, return_bar)
        self.assertEqual(hooked(), 'BAR')

    def test_after_hook_and_reset(self):
        hooked = self._callFUT(return_foo)
        old = hooked.sethook(not_called)
        hooked.reset()
        self.assertIs(old, return_foo)
        self.assertIs(hooked.original, return_foo)
        self.assertIs(hooked.implementation, return_foo)
        self.assertEqual(hooked(), 'FOO')

    def test_original_cannot_be_deleted(self):
        hooked = self._callFUT(not_called)
        with self.assertRaises((TypeError, AttributeError)):
            del hooked.original

    def test_implementation_cannot_be_deleted(self):
        hooked = self._callFUT(not_called)
        with self.assertRaises((TypeError, AttributeError)):
            del hooked.implementation

    def test_no_args(self):
        with self.assertRaises(TypeError):
            self._callFUT()

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            self._callFUT(not_called, not_called)

    def test_w_implementation_kwarg(self):
        hooked = self._callFUT(implementation=return_foo)
        self.assertIs(hooked.original, return_foo)
        self.assertIs(hooked.implementation, return_foo)
        self.assertEqual(hooked(), 'FOO')

    def test_w_unknown_kwarg(self):
        with self.assertRaises(TypeError):
            self._callFUT(nonesuch=42)

class HookableTests(PyHookableTests):

    def _callFUT(self, *args, **kw):
        from zope.hookable import hookable
        return hookable(*args, **kw)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
