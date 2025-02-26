#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    [print(" ".join("{}".format(num) for num in row)) for row in matrix]
