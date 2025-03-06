#!/usr/bin/python3
"""
Rectangle module - this module defines the Rectangle class
that inherits from BaseGeometry class
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
