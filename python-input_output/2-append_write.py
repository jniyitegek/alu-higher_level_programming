#!/usr/bin/python3
"""
File Append Module

This module provides  a file. It is designed to handle UTF-8 encoded text
and appends the text to the end of the file. If , it creates a new file.

Functions:
    append_write(filename="", text=""): Appends to a file the number of
                                       characters written.

Example:
    To append the text "Hello again!" to a file named "output.txt", use:
    >>> append_write("output.txt", "Hello again!")
"""


def append_write(filename="", text=""):
    """
    Appends text to a file and returns the number of characters written.

    This function opens a (`a`), which adds the text to the end of the file
    without overwriting i. If the file does not exist, it creates a new file.
    The text is written using UTF-8 encoding.

    Args:
        filename (str): The path to the appended. Defaults to an empty string.
        text (str): The text to be . Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.

    Example:
        >>> append_write("output.txt", "Hello again!")
        # This will append "Hello again!" to output.txt and return 12
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
