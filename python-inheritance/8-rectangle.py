#!/usr/bin/python3
"""
Rectangle Inheritance Module

This module defines two classes:

- BaseGeometry: A base class that provides a method to validate integer values.
- Rectangle: A subclass of BaseGeometry that represents a rectangle with a specified width and height.

The Rectangle class ensures that width and height are positive integers using the integer_validator method
from BaseGeometry. It also implements methods to compute the area and return a string representation
of the rectangle.

Example Usage:
    >>> r = Rectangle(4, 6)
    >>> print(r)
    [Rectangle] 4/6
    >>> print(r.area())
    24

Classes:
    BaseGeometry:
        - Provides a method to validate integer values.
    Rectangle:
        - Inherits from BaseGeometry and represents a rectangle.

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
