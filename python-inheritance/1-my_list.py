#!/usr/bin/python3
"""Module for MyList class that inherits from list."""

class MyList(list):
    """A class that inherits from list and provides additional functionality."""

    def print_sorted(self):
        """Print the list in ascending sorted order.

        Assumes all elements in the list are of type int.
        """
        print(sorted(self))
