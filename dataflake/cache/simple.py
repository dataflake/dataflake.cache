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
""" Simple non-persistent caches

$Id$
"""

from dataflake.cache.interfaces import ICache
from zope.interface import implements

class SimpleCache(object):
    """ Simple instance-level cache
    """
    implements(ICache)

    def __init__(self):
        self.cache = {}

    def set(self, key, value):
        """ Store a key/value pair
        """
        self.cache[key] = value

    def get(self, key=None, default=None):
        """ Get value for the given key, or all values if no key is passed

        If no value is found the default value will be returned.
        """
        if key:
            return self.cache.get(key, default)
        else:
            return self.cache.values()[:]

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


CACHE = {}

class ModuleSimpleCache(SimpleCache):
    """ Simple module-level cache

    All cache instances share the module level cache. It is important 
    for the applications that use these cache instances to ensure the
    cache keys are unique across all applications.
    """
    implements(ICache)

    def __init__(self):
        self.cache = CACHE
