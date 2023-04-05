#!/usr/bin/python3
class LockedClass:
    try:
        __slots__ = ['first_name']
    except:
        raise AttributeError(f"{self.__class__.__name__} object does \
            not support attribute assignment")
