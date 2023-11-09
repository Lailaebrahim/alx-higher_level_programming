#!/usr/bin/python3
""" Module for a method that return true if
object is an instance of the class
or if the object is an instance of a class that inherited
of that class
"""


def is_kind_of_class(obj, a_class):
    """

    :param obj: object to check
    :param a_class: class to which will check
    :return: True or False
    """
    return isinstance(obj, a_class)
