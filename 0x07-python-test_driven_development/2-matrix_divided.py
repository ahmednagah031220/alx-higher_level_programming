#!/usr/bin/python3
"""
dividing the matrix by another matrix module
"""

def matrix_divided(matrix, div):
    """
    dividing the matrix with the div

    Args:
        matrix: matrix to divide
        div: the divided matrix

    Return:
        return the list of the values
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for list_t in matrix:
        lenght = len(matrix[0])
        if not isinstance(list_t, list) or len(list_t) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(list_t) != lenght:
            raise TypeError("Each row of the matrix must have the same size")

        for value in list_t:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(value / div, 2) for value in list_t] for list_t in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
