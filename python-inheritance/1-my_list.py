#!/usr/bin/python3
"""
This module defines the MyList class, a subclass of the built-in list.
MyList includes a method to print its elements in ascending sorted order.
"""


class MyList(list):
    """
    A subclass of the built-in list class, with an additional method to
    print the elements of the list in ascending order.
    """

    
    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.

        This method does not modify the original list; it only displays a
        sorted version of the list.
        """
        print(sorted(self))  # Use the sorted() function to sort the list
