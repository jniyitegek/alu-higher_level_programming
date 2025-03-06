#!/usr/bin/python3
"""
Rectangle and Square Inheritance Module

This module defines three classes:

- BaseGeometry: A base class that provides a method to validate integer values.
- Rectangle: A subclass of BaseGeometry that represents a rectangle with a specified width and height.
- Square: A subclass of Rectangle that represents a square with a specified size.

The Rectangle and Square classes ensure that their dimensions are positive integers using the integer_validator method
from BaseGeometry. Both classes implement methods to compute the area and return a string representation
of their dimensions.

Example Usage:
    >>> r = Rectangle(4, 6)
    >>> print(r)
    [Rectangle] 4/6
    >>> print(r.area())
    24
    
    >>> s = Square(5)
    >>> print(s)
    [Square] 5/5
    >>> print(s.area())
    25

Classes:
    BaseGeometry:
        - Provides a method to validate integer values.
    Rectangle:
        - Inherits from BaseGeometry and represents a rectangle.
    Square:
        - Inherits from Rectangle and represents a square.

BaseGeometry Methods:
    integer_validator(name, value):
        - Ensures the value is a positive integer.

Rectangle Methods:
    __init__(self, width, height):
        - Initializes a rectangle with validated width and height.
    area(self):
        - Returns the area of the rectangle.
    __str__(self):
        - Returns a string representation of the rectangle.

Square Methods:
    __init__(self, size):
        - Initializes a square with validated size.
    area(self):
        - Returns the area of the square.
    __str__(self):
        - Returns a string representation of the square.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than zero.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""
    
    def __init__(self, size):
        """
        Initialize a Square instance.
        
        Args:
            size (int): The size of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than zero.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
