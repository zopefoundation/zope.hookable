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

$Id$
"""

from zope.testing.doctest import ELLIPSIS
from zope.testing.doctest import IGNORE_EXCEPTION_DETAIL
from zope.testing.doctestunit import DocTestSuite

def test_suite():
    return DocTestSuite('zope.hookable',
                        optionflags=ELLIPSIS|IGNORE_EXCEPTION_DETAIL,
                       )

if __name__ == '__main__':
    import unittest
    unittest.main()
