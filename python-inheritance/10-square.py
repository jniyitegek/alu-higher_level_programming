#!/usr/bin/python3
"""
This module contains the definition of the `Square` class, which is a specialized
version of the `Rectangle` class. It validates the size attribute, computes
the area, and provides a string representation of the square.

Classes:
    Rectangle: A class that defines a rectangle. Assumes width and height must
               be validated as positive integers.
    Square: A class that defines a square, inheriting from the Rectangle class.

Usage:
    Create a Square instance by providing a positive integer as size:
        square = Square(5)
    Compute the area of the square:
        print(square.area())
    Get the string representation of the square:
        print(square)
"""
class Rectangle:
    """
    A class representing a rectangle. Provides integer validation for its
    attributes and functionality to compute area and provide a string
    representation.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """
        Validates that the given value is a positive integer.

        Args:
            name (str): The name of the attribute being validated.
            value (int): The value of the attribute.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle, calculated as width × height.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A formatted string displaying the rectangle's dimensions.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """
    A class representing a square, which is a specific type of rectangle with
    equal width and height. Inherits from the Rectangle class.

    Provides validation for the square's size, computes its area, and returns
    a string representation.
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size (length of a side) of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square, calculated as size × size.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A formatted string displaying the square's dimensions.
        """
        return f"[Square] {self.__size}/{self.__size}"
