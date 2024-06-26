#!/usr/bin/python3
""" 
This module supplies on function, matrix_divided(). For example,
>>> matrix = [
	[1, 2, 3],
	[4, 5, 6]
]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by "div"
    checks if the entire list is int/float
    checks if each list in the matrix are the same size
    checks if "div" is an int/float or is 0
    """
    mes0 = "matrix must be a matrix (list of lists) of integers/floats"
    mes1 = "Each row of the matrix must have the same size"
    res_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(mes1)
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(mes0)
            else:
                inner_list.append(round(items / div, 2))
        res_matrix.append(inner_list)

    return res_matrix
