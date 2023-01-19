#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # The function uses a for loop to iterate over each row in the matrix.
        print(' '.join("{:d}".format(val) for val in row))
        # For each row, it calls ' '.join(...) which joins all elements
        # of the row using a space separator.
        # The format() method replaces the placeholder with the item from
        # the row, then the string passed to join() function to be joined.
        # The function will output the integers of the matrix, one row per line,
        # with elements in the row separated by a space.
