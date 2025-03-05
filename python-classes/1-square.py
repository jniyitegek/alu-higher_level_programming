#!/usr/bin/python3
"""
Module that defines a Square class with a private size attribute.

This module contains a simple Square class implementation that
initializes each instance with a given size.
"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): Private attribute for the size of the square.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.
        
        Args:
            size: The size of the square.
                  No type verification is done on size.
        """
        self.__size = size#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size
