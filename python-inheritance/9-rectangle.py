#!/usr/bin/python3
"""
This module defines two classes: BaseGeometry and Rectangle.

Classes:
    - BaseGeometry: Provides a method for validating integer values.
    - Rectangle: Inherits from BaseGeometry and represents a rectangle.

BaseGeometry includes:
    - integer_validator(name, value): Ensures value is a positive integer.

Rectangle includes:
    - __init__(self, width, height): Initializes a rectangle with validated width and height.
    - area(self): Returns the area of the rectangle.
    - __str__(self): Returns a string representation of the rectangle in the format [Rectangle] width/height.
"""

class BaseGeometry:
    """BaseGeometry class with validation methods."""
    def integer_validator(self, name, value):
        """Validates that a value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize the rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description in the format [Rectangle] width/height."""
        return f"[Rectangle] {self.__width}/{self.__height}"
