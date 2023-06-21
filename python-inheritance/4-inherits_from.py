#!/usr/bin/python3
"""object is an  instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
