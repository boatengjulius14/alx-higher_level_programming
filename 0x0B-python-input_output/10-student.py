#!/usr/bin/python3
"""Defines class Student"""


class Student:
    """Definition of Student class"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """returns a dictionary representation of
        an instance"""
        if isinstance(attrs, list):
            if all(isinstance(i, str) for i in attrs):
                return {i: self.__dict__[i] for i in \
attrs if i in self.__dict__}
        return self.__dict__
