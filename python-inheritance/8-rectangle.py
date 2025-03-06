#!/usr/bin/python3
"""
Module: rectangle
Defines a Rectangle class that inherits from BaseGeometry.
"""


class BaseGeometry:
    """
    Base class for geometry objects with validation functionality.
    """

    def integer_validator(self, name, value):
        """
        Validates that a parameter is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry for validation.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Validates and sets the width and height as private attributes.

        Args:
            width (int): The width of the rectangle. Must be a positive integer.
            height (int): The height of the rectangle. Must be a positive integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: Rectangle details in the format [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


# Testing instantiation to ensure it works as expected
rect = Rectangle(3, 5)
print(rect)  # Expected output: [Rectangle] 3/5
print(rect.area())  # Expected output: 15
