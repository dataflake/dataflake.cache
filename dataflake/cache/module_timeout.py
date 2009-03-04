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
""" A simple non-persistent thread-independent cache with timeout

$Id$
"""

import time

from dataflake.cache.interfaces import ITimeoutCache
from zope.interface import implements

MAX_SECS = 2147483647
CACHE = {}
TIMEOUTS = {}


class ModuleTimeoutCache(object):
    """ Simple module-level cache with timeout

    All cache instances share the module level cache. It is important 
    for the applications that use these cache instances to ensure the
    cache keys they use are unique.
    """
    implements(ITimeoutCache)

    def __init__(self):
        self.timeout = 600

    def set(self, key, object):
        key = key.lower()
        CACHE[key] = object
        TIMEOUTS[key] = time.time()

    def get(self, key=None, default=None):
        if key:
            key = key.lower()
            value = CACHE.get(key, None)

            if value is None:
                return default

            if time.time() < TIMEOUTS.get(key, MAX_SECS) + self.timeout:
                return value
            else:
                self.invalidate(key)
                return default
        else:
            now = time.time()
            return [x[1] for x in CACHE.items()
                     if now < TIMEOUTS.get(x[0], MAX_SECS) + self.timeout]

    def invalidate(self, key=None):
        if key is not None:
            key = key.lower()
            if CACHE.has_key(key):
                del CACHE[key]
            if TIMEOUTS.has_key(key):
                del TIMEOUTS[key]
        else:
            CACHE.clear()
            TIMEOUTS.clear()

    def setTimeout(self, timeout):
        self.timeout = timeout

