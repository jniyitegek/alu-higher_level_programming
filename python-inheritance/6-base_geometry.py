#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Calculate the area.

        Raises:
            Exception: Always raises an  'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
