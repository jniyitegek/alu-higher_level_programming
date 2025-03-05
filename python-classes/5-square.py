#!/usr/bin/python3
"""Square module.

This module provides a Square class for representing squares in a
geometric context. Each square has a size property with getter and setter
methods that include validation, and methods to calculate area and print
a representation of the square.
"""


class Square:
    """Define a square by its size.

    This class represents a square with a private size attribute accessible
    through property methods. The size is validated for integer type and
    non-negative value. The class can calculate the area of the square and
    print a representation of the square using # characters.

    Attributes:
        __size (int): Private instance attribute for the square's side length.
    """
 
    def __init__(self, size=0):
        """Initialize a new Square with the given size.
        
        Args:
            size (int, optional): The length of each side of the square.
                                  Defaults to 0.
        """
        self.size = size

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

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters.

        Prints a square using # characters with sides of length size.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
