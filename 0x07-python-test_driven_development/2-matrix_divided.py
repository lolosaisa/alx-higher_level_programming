#!/usr/bin/python3
""" Matrix_divided method module."""

def matrix_divided(matrix, div):
    """ It divides all elements of a given matrix by div.
    Args:
       matrix: list of lists containing int or float
       div: number to divide matrix by
    Returns:
       list: Lists of lits representing the divided matrix
    Raises:
       TypeError: if matrix is not a list containing int or float.
       TypeError: if sublists are not the same size
       TypeError: if div is not int or float
       ZeroDivisionError: if div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " + 
                "of integers/floats")

        for row in matrix:
            if not isinstance(row, list) or len(row) == 0:
                 raise TypeError("matrix must be a matrix (list of lists) " + 
                         "of integers/floats")
            if len(row) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
            for x in row:
                 if not isinstance(x, (int, float)):
                     raise TypeError("matrix must be a matrix (list of lists) " + 
                             "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
