#!/usr/bin/python3
"""
JSON Serialization Module

This module provides a a Python object into a JSON-formatted string.
It uses the `json` module from the Python to perform the serialization.

Functions:
    to_json_string(my_obj): Converts a Python object  string.

Example:
    To convert a dictionary into a JSON string, use:
    >>> to_json_string({"name": "John", "age": 30})
"""

def to_json_string(my_obj):
    """
    Converts a Python object into a JSON-formatted string.

    This object (e.g., dictionary, list, string, etc.) and serializes it
    into a JSON-formatted string using the `json.dumps()` method.

    Args:
        my_obj (any): The Python object to be serialized into a JSON string.

    Returns:
        str: A JSON-formatted string representing the input object.

    Example:
        >>> to_json_string({"name": "John", "age": 30})
        '{"name": "John", "age": 30}'
    """
    import json
    return json.dumps(my_obj)
