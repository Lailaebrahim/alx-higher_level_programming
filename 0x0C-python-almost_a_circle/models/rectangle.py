#!/usr/bin/python3
"""Module for Rectangle class which is a subclass of Base class"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle object.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The Height of the new Rectangle.
            x (int): The x Coordinate of the new Rectangle.
            y (int): The y Coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.

        Raises:
            TypeError: if width or height is not an int.
            TypeError: if x or y is not an int.
            ValueError: if width or height is <= 0.
            ValueError: if x or y < 0

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle and check it."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of the rectangle and check it."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """set x coordinate of the rectangle and check it."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y coordinate of the rectangle and check it."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method that returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Method to Print rectangle with # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        new_line = self.height - 1
        if self.y > 0:
            for yy in range(self.y):
                print()
        for hh in range(self.height):
            if self.x > 0:
                for xx in range(self.x):
                    print(" ", end="")
            for ww in range(self.width):
                print("#", end="")
            if new_line > 0:
                print()
                new_line -= 1

    def update(self, *args):
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
        else:
            raise ValueError("update() expects 5 arguments")

    def __str__(self):
        """Magic function to handle calling print function on rectangle object"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
