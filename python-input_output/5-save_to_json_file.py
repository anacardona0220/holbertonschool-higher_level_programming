#!/usr/bin/python3
"""a function that returns an object represented by a JSON string:"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to save the JSON representation.

    Returns:
        None
    """
    with open(filename, "w") as archivo:
        json.dump(my_obj, archivo)
