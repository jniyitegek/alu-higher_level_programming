#!/usr/bin/python3
"""Square module.

This module provides a Square class for representing squares in a
geometric context. Each square has a size that is set upon initialization
with type and value validation, and can calculate its area.
"""


class Square:
    """Define a square by its size.

    This class represents a square with a private size attribute.
    The size is set during initialization with validation for integer type
    and non-negative value. The class can calculate the area of the square.

    Attributes:
        __size: Private instance attribute representing the square's
                side length.
    """

    def __init__(self, size=0):
        """Initialize a new Square with the given size.

        The size parameter is validated and stored as a private attribute.

        Args:
            size (int, optional): The length of each side of the square.
                                  Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
