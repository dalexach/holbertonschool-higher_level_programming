#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for col in row:
            leng = len(row)
            i += 1
            print('{:d}'.format(col), end='')
            if i != leng:
                print(' ', end='')
        print('')
