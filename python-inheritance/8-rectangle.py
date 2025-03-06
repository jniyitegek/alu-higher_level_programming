#!/usr/bin/python3
"""
Rectangle Module

This module defines a Rectangle class that inherits from the BaseGeometry class
defined in the `7-base_geometry` module. The Rectangle class represents a rectangle
shape and includes methods for initializing and validating its dimensions.

Classes:
    Rectangle: A class that represents a rectangle and inherits from BaseGeometry.

Dependencies:
    The BaseGeometry class is imported from the `7-base_geometry` module.
"""

from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    This class represents a rectangle and includes methods for initializing
    and validating its width and height.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a Rectangle instance with
            validated width and height.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
