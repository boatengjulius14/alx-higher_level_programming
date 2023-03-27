#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        nb_print = 0
        for i in range(x):
            print(my_list[i], end="")
            nb_print += 1
        print()
        return nb_print
    except IndexError:
        print()
        return nb_print
