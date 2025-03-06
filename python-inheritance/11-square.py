#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description in the format [Square] <width>/<height>."""
        return f"[Square] {self.__size}/{self.__size}"
