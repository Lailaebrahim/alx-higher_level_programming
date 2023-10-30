#!/usr/bin/python3
"""Module for a Rectangle class."""


class Rectangle:
    """A class to represent rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

           Args:
               width (int): The width of the new rectangle.
               height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width value

            Returns:
                value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width value

            args:
                value: new value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

           Returns:
                value of height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle.
            args:
                value : of height.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
