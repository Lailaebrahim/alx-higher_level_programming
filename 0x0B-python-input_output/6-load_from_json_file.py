#!/usr/bin/python3
"""
Module to define a method that creates an
Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    Method that creates an
    Object from a JSON file
    :param filename: name of file to create from it
    :return python object of json file content
    """
    with open(filename) as file:
        return json.load(file)
