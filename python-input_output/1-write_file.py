#!/usr/bin/python3
"""
File Writer Module

This module to a file. It is designed to handle UTF-8 encoded text
and overwrites  it already exists. If the file does not exist, it creates
a new file.


Functions:
    write_file(filename="", text=""): Writes  and returns the number of
                                     characters written.

Example:
    To write the text "Hello, World!" to a file named "output.txt", use:
    >>> write_file("output.txt", "Hello, World!")
"""

def write_file(filename="", text=""):
    """
    Writes text to a file and returns the number of characters written.

    This function opens a file in write mode (`w`), overwriting its contents if it already exists.
    If the file does not exist, it creates a new file. The using UTF-8 encoding.

    Args:
        filename (str): The path will be written. Defaults to an empty string.
        text (str): The text to be written to the file.  string.

    Returns:
        int: The number of characters written to the file.

    Example:
        >>> write_file("output.txt", "Hello, World!")
        # This will write "Hello, World!" to output.txt and return 13
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
