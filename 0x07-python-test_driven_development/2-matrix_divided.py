#!/usr/bin/python3
"""
function that divides all element of a matrix
"""



def matrix_divided(matrix, div):
    """
    Function to divide all elm of a matrix
    
    Args: 
        matrix(list)
        div(int/float)
    
    Raises:
    if element of lists is not int/float:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
    if row is not the same size:
        TypeError: Each row of the matrix must have the same size
    if div is not int/float:
        TypeError: must be a number
    if div is not 0:
        ZeroDivisionError: division by zero
    Returns a new matrix
    """ 
    if not all(isinstance(row, list) or
               not all(isinstance(elm, (int, float))
                   for elm in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix_result = [[round(element / div, 2) for element in row] for row in matrix]
    return matrix_result
