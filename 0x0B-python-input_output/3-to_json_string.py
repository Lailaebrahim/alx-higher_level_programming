#!/usr/bin/python3
"""
Module to define a method that return
JSON representation of an obj (string)
"""


import json


def to_json_string(my_obj):
    """
    Method that return the JSON representation of an object (string)
    :param my_obj: object to return it's JSON representation
    :return: JSON representation of an object (string)
    """
    return json.dumps(my_obj)
