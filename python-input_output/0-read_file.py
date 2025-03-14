#!/usr/bin/python3
"""
File Reader Module

This module provides a function to read file to stdout.
It is designed to handle UTF-8 for common file-related issues.

Functions:
    read_file(filename=""): Reads a text file and to stdout.

Example:
    To read and of a file named "example.txt", use:
    >>> read_file("example.txt")
"""


def read_file(filename=""):
    """
    Reads a text file  its contents to stdout.
<<<<<<< HEAD

=======

>>>>>>> 73eb92e0dc521602f67c878eed502f45728488ca
    This function UTF-8 encoding, reads the entire
    content, and prints output without adding an extra
    newline at the end.

    Args:
        filename (str): The path. Defaults to an empty string.

    Returns:
        None


    Raises:
        FileNotFoundError: If the specified file does not exist.
<<<<<<< HEAD
        PermissionError: If the file due to permission issues.
        UnicodeDecodeError: If that cannot be decoded with UTF-8.

=======
        PermissionError: If the file cannot to permission issues.
        UnicodeDecodeError: If the file decoded with UTF-8.

>>>>>>> 73eb92e0dc521602f67c878eed502f45728488ca
    Example:
        >>> read_file("example.txt")
        # This will print the contents of example.txt to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
