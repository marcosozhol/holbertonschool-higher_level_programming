#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    s = []  # sera la nueva matriz
    for i in matrix:
        s.append(list(map(lambda x: x**2, i)))
    return s
