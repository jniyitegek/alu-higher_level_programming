#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """Check if inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if `obj` is an inherited from `a_class`; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
