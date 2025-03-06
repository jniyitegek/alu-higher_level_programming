#!/usr/bin/python3
"""Module for Rectangle class that inherits from BaseGeometry.

This module defines a Rectangle class that inherits from the BaseGeometry class.
It represents a rectangle with a given width and height, which are validated to
ensure they are positive integers. The width and height are private attributes
and do not have getters or setters.

Example:
    To use the Rectangle class, instantiate it with a width and height:

        r = Rectangle(5, 10)
        print(r.__dict__)  # Output: {'_Rectangle__width': 5, '_Rectangle__height': 10}
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry.

    This class represents a rectangle with a given width and height. The width
    and height are validated to ensure they are positive integers and are stored
    as private attributes.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            Exception: If width or height is not a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
