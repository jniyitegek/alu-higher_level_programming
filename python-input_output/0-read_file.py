#!/usr/bin/python3
"""
File Reader Module

This module provides a function to read file to stdout.
It is designed to handle UTF-8 for common file-related issues.

Functions:
    read_file(filename=""): Reads a text file and to stdout.

Example:
    To read and print the contents of a file named "example.txt", use:
    >>> read_file("example.txt")
"""

def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.
 
    This function opens a text file using UTF-8 encoding, reads the entire
    content, and prints it to the standard output without adding an extra
    newline at the end.
    
    Args:
        filename (str): The path. Defaults to an empty string.
        
    Returns:
        None
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the file cannot to permission issues.
        UnicodeDecodeError: If the file cannot be decoded with UTF-8.
        
    Example:
        >>> read_file("example.txt")
        # This will print the contents of example.txt to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
