#!/usr/bin/python3
"""
Module: rectangle
==================
This module defines the Rectangle class, which is a subclass of BaseGeometry. 
The Rectangle class provides functionality for creating and validating rectangles 
based on width and height dimensions.

Classes:
--------
    Rectangle
        Inherits from BaseGeometry and adds specific functionality for 
        handling rectangle dimensions, including initialization and validation.

Usage:
------
To use the Rectangle class, ensure that the '7-base_geometry' module is available 
and contains the necessary BaseGeometry implementation. Import and initialize 
Rectangle with valid integer dimensions:

    Example:
        >>> from rectangle import Rectangle
        >>> rect = Rectangle(5, 10)
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


