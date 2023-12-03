#!/usr/bin/python3
"""
Module to define a method that write to a file
"""

def write_file(filename="", text=""):
    """
    Method to write to a text file
    :param filename: a string that is the path of the text file to write to
    :param text: text to be written
    :return: number of written characters
    """
    with open(filename, "w") as file:
        return file.write(text)
