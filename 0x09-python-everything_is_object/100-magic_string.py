#!/usr/bin/python3
def magic_string():
    magic_string.mul = getattr(magic_string, 'mul', 0) + 1
    return "BestSchool, " * (magic_string.mul - 1) + "BestSchool"
