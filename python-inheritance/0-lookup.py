#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    This function uses the built-in `dir()` function to retrieve the attributes
    and methods of the given object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of strings representing the names of the attributes and methods
              of the object.
    """
    return dir(obj)
