#!/usr/bin/python3
"""
Module to returns the dictionary description of the obj
    where all the keys or values are JSON serializable.
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description of the obj
    where all the keys or values are JSON serializable.
    :param obj: object to return its dictionary representation.
    :return: dictionary representation.
    """
    return obj.__dict__
