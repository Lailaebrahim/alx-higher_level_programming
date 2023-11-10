#!/usr/bin/python3
"""Module for Square class which is a subclass of Rectangle class"""
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Rectangle object.

            Args:
                size (int): The size of the new Square.
                x (int): The x Coordinate of the new Square.
                y (int): The y Coordinate of the new Square.
                id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set/get Size of the Square object"""
        return self.width

    @size.setter
    def size(self, value):
        """set width and height to size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that  that assigns an argument to each attribute.
        Args:
            *args (ints) :
                1st argument should be the id attribute
                2nd argument should be the size attribute
                4th argument should be the x attribute
                5th argument should be the y attribute

            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """Magic function to handle calling print function on square object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
