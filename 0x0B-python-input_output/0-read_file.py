#!/usr/bin/python3
"""
Module to define a mehthod that read from a file
"""


def read_file(filename=""):
    """
    Method to read from a text file
    :param filename: a string that is the path of the text file to read from
    :return: No return
    """
    with open(filename, "r") as file:
        print(file.read(), end="")
