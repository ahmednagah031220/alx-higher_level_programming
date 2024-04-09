#!/usr/bin/python3
"""
Printing a square
"""

def print_square(size):
    """
    Printing a square
    Args:
        size: the size length of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n") * size, end='')

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
