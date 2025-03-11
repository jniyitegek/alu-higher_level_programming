#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    This function opens a text file using UTF-8 encoding, reads the entire
    content, and prints it to the standard output without adding an extra
    newline at the end.

    Args:
        filename (str): The path to the file to be read. Defaults to an empty string.
        
    Returns:
        None


    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the file cannot be accessed due to permission issues.
        UnicodeDecodeError: If the file contains characters that cannot be decoded with UTF-8.

    Example:
        >>> read_file("example.txt")
        # This will print the contents of example.txt to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
