#!/usr/bin/python3
"""A module for square"""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Constructor.
        Args:
            size: length of side of the square.
        """
        self.size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size)**2

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the current size of the square."""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
