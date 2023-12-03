#!/usr/bin/python3
"""
Module to define a method that writes
Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Method that writes Object to a text file,
    using a JSON representation
    :param my_obj: object to write to the file
    :param filename: name of file to write to it
    :return: JSON representation of an object (string)
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
