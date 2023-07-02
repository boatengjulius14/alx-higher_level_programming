#!/usr/bin/python3
"""find_peak finds the peak in a list"""


def find_peak(list_of_integers):
    """finds a peak in a list unsorted integers"""
    if list_of_integers:
        low = 0
        high = len(list_of_integers) - 1
        while low < high:
            mid = (low + high) // 2
            if list_of_integers[mid] >= list_of_integers[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return list_of_integers[low]
    return None
