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
        Constructor
        :param first_name: first name of student
        :param last_name: last name of student
        :param age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A method that retrieves a dictionary rep of a Student
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        :param attrs:
        :return:
        """
        dic = {}
        if isinstance(attrs, list):
            if all(isinstance(item, str) for item in attrs):
                for item in attrs:
                    if item in ['first_name', 'last_name', 'age']:
                        if item == "first_name":
                            dic.update(first_name=self.first_name)
                        elif item == "last_name":
                            dic.update(last_name=self.last_name)
                        elif item == "age":
                            dic.update(age=self.age)
            return dic
        else:
            return self.__dict__
