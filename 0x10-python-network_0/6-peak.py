#!/usr/bin/python3
"""
Function that finda a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
        Find a peak
        list_of_integers: list if unsirted integers
    """
    ll = len(list_of_integers)
    if ll == 0:
        return
    h = ll // 2
    if (h == ll - 1 or list_of_integers[h] >=
        list_of_integers[h + 1]) and (h == 0 or list_of_integers[h] >=
                                      list_of_integers[h - 1]):
        return (list_of_integers[h])
    elif h != ll - 1 and list_of_integers[h + 1] > list_of_integers[h]:
        return (find_peak(list_of_integers[h + 1:]))
    else:
        return (find_peak(list_of_integers[:h]))
