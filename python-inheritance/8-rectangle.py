#!/usr/bin/python3
"""
Rectangle Inheritance Module

This module defines a BaseGeometry class that provides integer validation
and a Rectangle class that inherits from BaseGeometry. The Rectangle class
represents a rectangle with a specified width and height, ensuring they
are positive integers.

Example:
    To create a Rectangle instance:

        r = Rectangle(4, 6)
        print(r)  # Output: [Rectangle] 4/6
        print(r.area())  # Output: 24

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
    """Rectangle class that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize a Rectangle instance with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a formatted string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
