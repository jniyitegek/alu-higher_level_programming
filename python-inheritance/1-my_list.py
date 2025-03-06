#!/usr/bin/python3
"""
Module: 1-my_list.py

This module defines the MyList class, which extends the built-in list class
and includes a method to print the list in ascending sorted order.

Usage Example:
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)          # Prints the original list
    my_list.print_sorted()  # Prints the sorted list
    print(my_list)          # Prints the original list unchanged
"""

class MyList(list):
    """A subclass of list with an additional method to print a sorted version of the list."""
    
    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))

# Example usage
if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
