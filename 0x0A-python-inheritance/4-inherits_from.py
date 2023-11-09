#!/usr/bin/python3
""" Module for a method that return true if
if the object is an instance of a class that
inherited (directly or indirectly) from the
specified class otherwise False.
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the
    specified class otherwise False
    :param obj: The object to check
    :param a_class: Class used for checking
    :return: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
