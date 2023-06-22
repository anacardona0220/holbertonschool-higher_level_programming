#!/usr/bin/python3
'''function that returns the JSON representation of an object (string)'''
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    json_string = json.dumps(my_obj)
    return json_string
