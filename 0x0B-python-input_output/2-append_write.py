#!/usr/bin/python3
"""
Module to define a method that append to a file
"""


def write_file(filename="", text=""):
    """
    Method to write to a text file
    :param filename: a string that is the path of the text file to append to
    :param text: text to be appended
    :return: number of appended characters
    """
    with open(filename, "a") as file:
        return file.write(text)
