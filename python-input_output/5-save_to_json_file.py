#!/usr/bin/python3
"""
JSON File Serialization Module

This module provides a Python object as a JSON-formatted string to a file.
It uses the `json` module from the library to perform the serialization.

Functions:
    save_to_json_file(my_obj, filename):  as a JSON-formatted string to a file.

Example:
    To save a dictionary as a  to a file named "data.json", use:
    >>> save_to_json_file({"name": "John", "age": 30}, "data.json")
"""


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object as a JSON-formatted string to a file.

    This object (e.g., dictionary, list, string, etc.) and serializes it
    into a JSON-formatted string, which is then written. If the file already
    exists, it will be overwritten.

    Args:
        my_obj (any): The Python object to be serialized into a JSON string.
        filename (str): The path to the file where the JSON string will .

    Returns:
        None

    Example:
        >>> save_to_json_file({"name": "John", "age": 30}, "data.json")
        # This will save the dictionary as a JSON string to "data.json"
    """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
