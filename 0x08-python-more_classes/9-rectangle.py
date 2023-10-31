#!/usr/bin/python3
"""Module for a Rectangle class."""


class Rectangle:
    """A class to represent rectangle.

       Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any type): Used as symbol for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

           Args:
               width (int): The width of the new rectangle.
               height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
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

    def area(self):
        """a method to return area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """a method to return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a Rectangle with width and height equal to size.

        Args:
            size (int): size of square.
        """
        return (cls(size, size))

    def __str__(self):
        """Return a human readable format of object of rectangle class"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ('\n'.join([str(self.print_symbol)
                           * self.__width] * self.__height))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return ("Rectangle(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        """Print a message for deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
