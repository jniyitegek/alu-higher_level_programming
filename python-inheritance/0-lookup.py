#!/usr/bin/python3
"""Module for inspecting objects and retrieving their attributes and methods.

This module provides a function `lookup` that returns a list of available
attributes and methods built-in `dir()` function.
"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    This function uses the built-in `dir()` function to retrieve the attributes
    and methods of the given object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of strings  the attributes and methods
              of the object.
    """
    return dir(obj)
