#!/usr/bin/python3
"""Square module.

This module provides a Square class for representing squares in a
geometric context. Each square has size and position properties with
getter and setter methods that include validation.
"""


class Square:
    """Define a square by its size and position.

    This class represents a square with private size and position attributes,
    accessible through property methods. Both attributes are validated.
    The class can calculate the area of the square and print a representation
    of the square using # characters at the specified position.

    Attributes:
        __size (int): Private instance attribute for the square's side length.
        __position (tuple): Private instance attribute for the square's position
                           as a tuple of 2 positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with the given size and position.

        Args:
            size (int, optional): The length of each side of the square.
                                  Defaults to 0.
            position (tuple, optional): The position of the square as a tuple
                                       of 2 positive integers. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the current size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the current position of the square.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): The new position for the square as a tuple
                          of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters.

        Prints a square using # characters with sides of length size,
        at the specified position. The horizontal position is represented
        by spaces, and the vertical position by new lines.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        # Print vertical offset
        for i in range(self.__position[1]):
            print()
        # Print the square with horizontal offset
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
