#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    if len(tuple_a) < 2:
        while len(tuple_a) != 2:
            tuple_a.append(0)
    if len(tuple_b) < 2:
        while len(tuple_b) != 2:
            tuple_b.append(0)
    if len(tuple_a) > 2:
        tuple_a[2:] = []
    if len(tuple_a) > 2:
        tuple_a[2:] = []
    sum_tuple = tuple([(tuple_a[i]+tuple_b[i]) for i in range(2)])
    return sum_tuple
