#!/usr/bin/python3
"""Module for BaseGeometry class."""

class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Calculate the area.

        Raises:
            Exception: Always raises an exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
