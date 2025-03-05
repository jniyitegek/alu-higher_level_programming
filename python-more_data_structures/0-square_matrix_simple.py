#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    
    Args:
        matrix (list): A 2 dimensional array of integers
        
    Returns:
        A new matrix of the same size with each value squared
    """
    if not matrix:
        return []
    
    new_matrix = []
    for row in matrix:
        new_row = list(map(lambda x: x ** 2, row))
        new_matrix.append(new_row)
    
    return new_matrix
