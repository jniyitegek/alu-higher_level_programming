#!/usr/bin/python3
"""Square module.

This module provides a Square class for representing squares in a
geometric context. Each square has a size that is set upon initialization.
"""


class Square:
    """Define a square by its size.

    This class represents a square with a private size attribute.
    The size is set during initialization and cannot be accessed directly.

    Attributes:
        __size: Private instance attribute representing the square's
                side length.
    """

    def __init__(self, size):
        """Initialize a new Square with the given size.

        The size parameter is stored as a private instance attribute.

        Args:
            size: The length of each side of the square.
                 No type or value verification is performed.

        Returns:
            None
        """
        self.__size = size
