#!/usr/bin/python3
"""
This module defines the Rectangle class, which is a subclass of BaseGeometry. 
It provides functionality for creating and validating rectangle dimensions.

Classes:
    Rectangle: Represents a rectangle using BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry for validation.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Validates and sets the width and height of the rectangle.

        Args:
            width (int): The width of the rectangle. Must be validated as an integer.
            height (int): The height of the rectangle. Must be validated as an integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

