#!/usr/bin/python3
"""a function that returns the list of available
attributes and methods of an object:"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    obj (object): The object to inspect.

    Returns:
    list: A list of strings representing the available
    attributes and methods of the object.
    """
    return dir(obj)
