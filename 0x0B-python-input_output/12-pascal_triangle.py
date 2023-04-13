#!/usr/bin/python3
"""Defines the function pascal_triangle"""


def pascal_triangle(n):
    """returns a list of list of integers"""
    if n <= 0:
        return []
    _list = [[]]
    for i in range(n):
        if i == 0:
            _list = [[1]]
        elif i == 1:
            _list.extend([[1, 1]])
        else:
            add = 0
            flag = 0
            _listadd = [1]
            j = 0
            while j < len(_list[-1]):
                add += _list[-1][j]
                flag += 1
                if flag == 2:
                    _listadd.extend([add])
                    flag = 0
                    add = 0
                    continue
                j += 1
            _listadd.append(1)
            _list.extend([_listadd])
    return _list


def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
