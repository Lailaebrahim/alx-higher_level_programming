#!/usr/bin/python3
"""module to implement a function that is able to
add new attributes for an object of predefined class without
using hasattr built-in function to check if we can add attribute
to that object
and setattr to set new attribute
"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object of a predefined class if possible.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
