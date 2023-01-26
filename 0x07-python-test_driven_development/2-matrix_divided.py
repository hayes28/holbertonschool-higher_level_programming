#!/usr/bin/python3
"""
    Divide all elements of a matrix
"""
type_error = "matrix must be a matrix (list of lists) of integers/floats"
size_error = "Each row of the matrix must have the same size"
num_error = "div must be a number"

def matrix_divided(matrix, div):
    """_summary_ Divide all elements of a matrix with a div

    Args:
        matrix (matrix of ints or floats): _description_
        div (int or float): _description_
    """
    if type(matrix) is not list:
        raise TypeError(type_error)
    size = len(matrix[0])

    for row in matrix:
        if len(row)!= size:
            raise TypeError(size_error)
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError(type_error)
        if type(div) is not int and type(div) is not float:
            raise TypeError(num_error)
        if div == 0:
            raise ZeroDivisionError("division by zero")
        return [[round(i / div, 2) for i in row] for row in matrix]
