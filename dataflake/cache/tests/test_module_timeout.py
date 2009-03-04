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
""" Tests for the ModuleTimeout cache class

$Id$
"""

import time
import unittest

from dataflake.cache.tests.base import CacheTests

       
class TestTimeoutCache(CacheTests):

    def _getTargetClass(self):
        from dataflake.cache.module_timeout import ModuleTimeoutCache
        return ModuleTimeoutCache

    def test_conformance(self):
        from dataflake.cache.interfaces import ITimeoutCache
        from zope.interface.verify import verifyClass
        verifyClass(ITimeoutCache, self._getTargetClass())

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

    def test_timeout(self):
        # initial state
        self.assertEquals(self.cache.timeout, 600)

        self.cache.setTimeout(0.1)
        self.assertEquals(self.cache.timeout, 0.1)

        self.cache.set('key1', 'value1')
        self.assertEquals(self.cache.get(), ['value1'])
        self.assertEquals(self.cache.get('key1'), 'value1')

        # Wait for the timeout. The key must be gone.
        time.sleep(0.3)
        self.failIf(self.cache.get())
        self.failIf(self.cache.get('key1'))


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(TestTimeoutCache),
        ))

