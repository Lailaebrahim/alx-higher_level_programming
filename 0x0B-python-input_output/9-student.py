#!/usr/bin/python3
"""
Module to returns the dictionary description of the obj
    where all the keys or values are JSON serializable.
"""


class Student:
    """
    Represent a student.
    """
    def __init__(self, first_name, last_name, age):
        """

        :param first_name: first name of student
        :param last_name: last name of student
        :param age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """

        :return: Dictionary representation of the Student obj.
        """
        dic = {"first_name": self.first_name, "last_name": self.last_name,
               "age": self.age}
        return dic
