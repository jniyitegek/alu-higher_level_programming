#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return  # Exit the function if the list is None

    for num in reversed(my_list):
        print("{:d}".format(num))
