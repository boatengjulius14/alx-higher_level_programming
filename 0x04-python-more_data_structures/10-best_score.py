#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = a_dictionary[list(a_dictionary)[0]]
    for i in a_dictionary:
        if a_dictionary[i] > max:
            key = i
    return key
