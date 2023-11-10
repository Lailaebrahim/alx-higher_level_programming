#!/usr/bin/python3
"""Module for Base class"""


class Base:
    """
    A base class This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all future classes
    and to avoid duplicating the same code.

    Attributes:
        __nb_objects (int): to store number of objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base object.

        Args:
             id (int): a specific id for each new object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
