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
""" A simple non-persistent cache with timout

$Id$
"""

import time

from dataflake.cache.interfaces import ITimeoutCache
from zope.interface import implements

MAX_SECS = 2147483647

class TimeoutCache(object):
    """ A simple non-persistent cache with timeout
    """
    implements(ITimeoutCache)

    def __init__(self):
        self.cache = {}
        self.timeouts = {}
        self.timeout = 600

    def set(self, key, object):
        key = key.lower()
        self.cache[key] = object
        self.timeouts[key] = time.time()

    def get(self, key=None, default=None):
        if key:
            key = key.lower()
            value = self.cache.get(key, None)

            if value is None:
                return default

            if time.time() < self.timeouts.get(key, MAX_SECS) + self.timeout:
                return value
            else:
                self.invalidate(key)
                return default
        else:
            now = time.time()
            return [x[1] for x in self.cache.items()
                     if now < self.timeouts.get(x[0], MAX_SECS) + self.timeout]

    def invalidate(self, key=None):
        if key is not None:
            key = key.lower()
            if self.cache.has_key(key):
                del self.cache[key]
            if self.timeouts.has_key(key):
                del self.timeouts[key]
        else:
            self.cache = {}
            self.timeouts = {}

    def setTimeout(self, timeout):
        self.timeout = timeout

