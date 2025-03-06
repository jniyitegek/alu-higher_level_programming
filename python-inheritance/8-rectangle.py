#!/usr/bin/python3
"""
Rectangle Module

This module defines a Rectangle class that inherits from the BaseGeometry class.
The Rectangle class represents a rectangle shape and includes methods for
initializing and validating its dimensions.

Classes:
    BaseGeometry: A base class for geometry-related operations.
    Rectangle: A class that represents a rectangle and inherits from BaseGeometry.
"""


class BaseGeometry:
    """
    BaseGeometry Class

    A base class for geometry-related operations. This class includes methods
    for validating integer values.
    """

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
