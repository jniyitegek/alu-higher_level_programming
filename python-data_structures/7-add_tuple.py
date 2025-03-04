#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuples have at least 2 elements, using 0 for missing elements
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Add first two elements and return as a new tuple
    return (a[0] + b[0], a[1] + b[1])
