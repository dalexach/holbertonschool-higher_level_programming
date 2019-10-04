#!/usr/bin/python3
"""
Divide a matrix module

This module divides all elements of a matrix.
Otherwise raise a TypeError exception or ZeroDivisionError exception
with custom error messages

"""


def matrix_divided(matrix, div):
    """
    Arguments:
    @matrix: must be a list of lists of integers or floats
    @div: must be a number (integer or float)

    Returns:
    A new matrix with all elements of matrix divided by div.
    Otherwise raise a TypeError exception if in matrix are not
    integers or floats, or ZeroDivisionError exception when an element
    is divided by 0.
    The result of division must be rounded to 2 decimal places.

    """
    new_matrix = []
    te = "matrix must be a matrix (list of lists) of integers/floats"
    le = "Each row of the matrix must have the same size"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(te)
    for element in matrix:
        if type(element) is not list:
            raise TypeError(te)
        for i in element:
            if type(i) is not int and type(i) is not float:
                raise TypeError(te)
            leng = len(matrix[0])
            if len(element) != leng:
                raise TypeError(le)
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for row in matrix:
        new_matrix.append(list(map(lambda x: round(x/div, 2), row)))
    return new_matrix
