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
""" Simple non-persistent caches with timeout

$Id$
"""

from threading import RLock
import time

from zope.interface import implements

from dataflake.cache.interfaces import ITimeoutCache
from dataflake.cache.utils import protect_with_lock

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
        """ Store a key/value pair
        """
        key = key.lower()
        self.cache[key] = object
        self.timeouts[key] = time.time()

    def get(self, key=None, default=None):
        """ Get value for the given key, or all values if no key is passed

        If no value is found or the value is older than the allowed 
        timeout, the default value will be returned.
        """
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
        """ Invalidate the given key, or all key/values if no key is passed.
        """
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
        """ Set a timeout value in seconds
        """
        self.timeout = timeout


class LockingTimeoutCache(TimeoutCache):
    """ Simple module-level cache protected by a lock serializing access

    All cache instances share the module level cache. It is important 
    for the applications that use these cache instances to ensure the
    cache keys are unique across all applications.
    """
    implements(ITimeoutCache)

    def __init__(self):
        super(LockingTimeoutCache, self).__init__()
        self.lock = RLock()

    @protect_with_lock
    def set(self, key, value):
        """ Store a key/value pair
        """
        return super(LockingTimeoutCache, self).set(key, value)

    @protect_with_lock
    def get(self, key=None, default=None):
        """ Get value for the given key, or all values if no key is passed

        If no value is found the default value will be returned.
        """
        return super(LockingTimeoutCache, self).get(key, default)

    @protect_with_lock
    def invalidate(self, key=None):
        """ Invalidate the given key, or all key/values if no key is passed.
        """
        return super(LockingTimeoutCache, self).invalidate(key)

