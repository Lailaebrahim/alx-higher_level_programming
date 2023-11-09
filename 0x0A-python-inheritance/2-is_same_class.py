#!/usr/bin/python3
""" Module for a method that return true if
object is an instance of the class
"""


def is_same_class(obj, a_class):
    """Method to return True if an object is exactly
    an instance of the class

    Args:
        obj : An object of any class
        a_class : Any class

    Return:
        True or False
    """
    if a_class == type(obj):
        return True
    else:
        return  False
