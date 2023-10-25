#!/usr/bin/python3
"""A module for square"""


class Square:
    """Represent a square."""
    def __init__(self, size):
        """Constructor.
        Args:
            size: length of side of the square.
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.SIZE = size
