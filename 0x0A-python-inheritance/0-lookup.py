#!/usr/bin/python3
def lookup(obj):
    """
       Get the attributes and methods of the object
       :param obj: an object
       :return: a list of all the attributes found for thr object
    """
    attributes_and_methods = dir(obj)
    filtered_attributes_and_methods = [item for item in attributes_and_methods if not item.startswith("__")]
    return filtered_attributes_and_methods
