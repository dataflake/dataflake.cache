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

from dataflake.cache.tests.base import CacheTestCase

       
class TestSimpleCache(CacheTestCase):

    def _getTargetClass(self):
        from dataflake.cache.simple import SimpleCache
        return SimpleCache

    def test_conformance(self):
        from dataflake.cache.interfaces import ICache
        from zope.interface.verify import verifyClass
        verifyClass(ICache, self._getTargetClass())

    def test_initial_state(self):
        self.failIf(self.cache.get())

    def test_get_set_clear(self):
        self.failIf(self.cache.get())

        self.cache.set('key1', 'value1')
        self.assertEquals(self.cache.get(), ['value1'])
        self.assertEquals(self.cache.get('key1'), 'value1')

        self.cache.set('key2', 'value2')
        self.assertEquals(set(self.cache.get()), set(['value1', 'value2']))
        self.assertEquals(self.cache.get('key2'), 'value2')

        self.cache.set('key3', 'value3')
        self.cache.invalidate('key1')
        self.assertEquals(set(self.cache.get()), set(['value2', 'value3']))
        self.failIf(self.cache.get('key1'))

        self.cache.set('key3', 'NEW')
        self.assertEquals(self.cache.get('key3'), 'NEW')

        self.cache.invalidate()
        self.failIf(self.cache.get())


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(TestSimpleCache),
        ))

