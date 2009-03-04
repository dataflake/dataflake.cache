##############################################################################
#
# Copyright (c) 2009 Jens Vagelpohl and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Tests for the Simple cache class

$Id$
"""

import unittest


class CacheTests(unittest.TestCase):

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def _getTargetClass(self):
        raise NotImplemented

    def setUp(self):
        self.cache = self._makeOne()

    def test_initial_state(self):
        self.failIf(self.cache.get())
