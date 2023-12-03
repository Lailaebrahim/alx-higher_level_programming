#!/usr/bin/python3
"""
Module to define a method that returns a python object represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Method that returns an object (Python data structure) represented by a JSON string
    :param my_str: object to return its python string representation
    :return: python string of a JSON representation (string)
    """
    return json.loads(my_str)
