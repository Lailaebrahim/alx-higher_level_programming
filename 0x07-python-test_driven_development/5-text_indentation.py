#!/usr/bin/python3
"""Module for text_indentation method.
   This module contain only one method that
   takes a text and add newlines after a delimiter
"""


def text_indentation(text):
    """This method take a text and put two newlines after certain delimiters

    Args:
        text : a string text

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
