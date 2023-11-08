#!/usr/bin/python3
"""Module to define a new SubClass of Superclass list """


class MyList(list):
    """A class to make a subclass of list class

   Methods:
        print_sorted :Method to sort list and printed
    """
    def print_sorted(self):
        """Method to sort list and print them sorted assuming the elements are all ints"""
        print(sorted(self))
