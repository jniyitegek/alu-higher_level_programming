#!/usr/bin/python3
"""Module for is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if `obj` is an instance from `a_class`; otherwise False.
    """
    return isinstance(obj, a_class)
