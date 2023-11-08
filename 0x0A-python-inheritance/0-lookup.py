#!/usr/bin/python3
"""Module for lookup method """
def lookup(obj):
    """
       Get the attributes and methods of the object
       :param obj: an object
       :return: a list of all the attributes found for thr object
    """
    attributes_and_methods = dir(obj)
    filtered_attributes_and_methods = [item for item in attributes_and_methods]
    return filtered_attributes_and_methods
