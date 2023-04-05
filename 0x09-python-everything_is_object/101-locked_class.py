#!/usr/bin/python3
"""locked class definition"""


class LockedClass:
    """
    Prevents the user from dynamically creating any instance attributes
    apart from 'first_name'
    """
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name != 'first_name' and not hasattr(self, 'first_name'):
            raise AttributeError(f"{self.__class__.__name__} object\
 does not support attribute assignment")
        super().__setattr__(name, value)
