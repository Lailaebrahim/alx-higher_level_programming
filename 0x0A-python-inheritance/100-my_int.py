#!/usr/bin/python3
"""module for MyInt Class that inherit from int class"""


class MyInt(int):
    """
    MyInt is a subclass of int class
    """
    def __eq__(self, value):
        """A method that revert the function of =="""
        return self.real != value

    def __ne__(self, value):
        """A method that revert the function of !="""
        return  self.real == value
