#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py)."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
<<<<<<< HEAD
=======

    def __str__(self):
        """Return the string representation of the square.

        Returns:
            str: The formatted string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
>>>>>>> 7a6747e03213d0b0d1b7a12e2424d227d9a75dd8
