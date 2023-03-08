#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for i in str:
        if i > 'Z':
            upper_str += chr(ord(i) - 32)
        else:
            upper_str += i
    print("{}".format(upper_str))
