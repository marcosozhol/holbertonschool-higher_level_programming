#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for columna in fila:
            print('{:d}'.format(columna), end=" "if columna != fila[-1] else"")
        print()
