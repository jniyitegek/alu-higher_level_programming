#!/usr/bin/python3
"""Module for MyList class that inherits from list.

This module defines a custom list class, `MyList`, which inherits from the built-in
`list` class. It provides an additional method, `print_sorted()`, to print the list
in ascending sorted order. This module assumes that all elements in the list are of
type `int`.
"""

class MyList(list):
    """A custom list class that inherits from the built-in `list` class.

    This class extends the functionality of the `list` class by adding a method
    to print the list in sorted order. It assumes that all elements in the list
    are of type `int`.

    Attributes:
        Inherits all attributes from the `list` class.
    """

    def print_sorted(self):
        """Print the list in ascending sorted order.

        This method sorts the list in ascending order and prints it. It does not
        modify the original list.

        Assumptions:
            All elements in the list are of type `int`.

        Example:
            >>> my_list = MyList()
            >>> my_list.append(3)
            >>> my_list.append(1)
            >>> my_list.append(2)
            >>> my_list.print_sorted()
            [1, 2, 3]
        """
        print(sorted(self))
