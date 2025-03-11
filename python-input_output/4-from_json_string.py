#!/usr/bin/python3
"""
JSON Deserialization Module

This module provides a convert a JSON-formatted string into a Python object.
It uses the `json` module  standard library to perform the deserialization.

Functions:
    from_json_string(my_str): Converts a  string into a Python object.

Example:
    To convert a JSON string into a Python dictionary, use:
    >>> from_json_string('{"name": "John", "age": 30}')
"""


def from_json_string(my_str):
    """
    Converts a JSON-formatted string into a Python object.

    This function takes a JSON-formatted string  it into a Python object
    (e.g., dictionary, list, string, etc.) using the `json.loads()` method.

    Args:
        my_str (str): The JSON-formatted string to be into a Python object.

    Returns:
        any: A Python object representing the data in the JSON string.

    Example:
        >>> from_json_string('{"name": "John", "age": 30}')
        {'name': 'John', 'age': 30}
    """
    import json
    return json.loads(my_str)
