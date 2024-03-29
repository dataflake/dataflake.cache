##############################################################################
#
# Copyright (c) 2009-2023 Jens Vagelpohl and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Simple non-persistent caches
"""

from threading import RLock

from zope.interface import implementer

from .interfaces import ICache
from .utils import protect_with_lock


@implementer(ICache)
class SimpleCache:
    """ Simple instance-level cache
    """

    def __init__(self):
        self.cache = {}

    def set(self, key, value):
        """ Store a key/value pair
        """
        self.cache[key] = value

    def get(self, key, default=None):
        """ Get value for the given key

        If no value is found the default value will be returned.
        """
        return self.cache.get(key, default)

    def invalidate(self, key=None):
        """ Invalidate the given key, or all key/values if no key is passed.
        """
        if key:
            try:
                del self.cache[key]
            except (KeyError, IndexError):
                pass
        else:
            self.cache = {}

    def keys(self):
        """ Return all cache keys
        """
        return self.cache.keys()

    def values(self):
        """ Return all cached values
        """
        return self.cache.values()

    def items(self):
        """ Return all cached keys and values

        Returns a sequence of (key, value) tuples.
        """
        return self.cache.items()


@implementer(ICache)
class LockingSimpleCache(SimpleCache):
    """ Simple module-level cache protected by a lock serializing access
    """

    def __init__(self):
        super().__init__()
        self.lock = RLock()

    @protect_with_lock
    def set(self, key, value):
        """ Store a key/value pair
        """
        return super().set(key, value)

    @protect_with_lock
    def get(self, key, default=None):
        """ Get value for the given key

        If no value is found the default value will be returned.
        """
        return super().get(key, default)

    @protect_with_lock
    def invalidate(self, key=None):
        """ Invalidate the given key, or all key/values if no key is passed.
        """
        return super().invalidate(key)
