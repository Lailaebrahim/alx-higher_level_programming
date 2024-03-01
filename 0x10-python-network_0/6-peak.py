#!/usr/bin/python3
"""Find peak of unsorted list"""
def find_peak(list_of_integers):
    """Method to find peak"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers
