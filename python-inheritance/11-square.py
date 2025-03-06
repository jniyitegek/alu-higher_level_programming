#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle.

This module defines a Square class that inherits from the Rectangle class
and represents a square with a given size. The size is validated to ensure
it is a positive integer, and the class provides methods for calculating
the area and returning a string representation of the square.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description in the format [Square] <width>/<height>.

        Returns:
            str: A string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
