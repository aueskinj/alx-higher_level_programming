#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    print("\n".join([" ".join("{:d}".format(col) for col in row) for row in matrix]))
