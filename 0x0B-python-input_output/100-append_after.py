#!/usr/bin/python3
"""Module to define a Method that insert
a text after a line containing a keyword.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename, "r") as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as file:
        file.write(text)
