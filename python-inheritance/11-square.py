#!/usr/bin/python3

"""
This module defines a Rectangle and Square class.

Rectangle includes attributes for width and height with validation.
Square inherits from Rectangle and enforces size validation.
"""


class Rectangle:
    """
    A class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.width}/{self.height}"


class Square(Rectangle):
    """
    A class that defines a square, inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with a given size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
