#!/usr/bin/python3

"""Peak finder function"""

def find_peak(list_of_integers):
    """Finds peak in unsorted integers list"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
