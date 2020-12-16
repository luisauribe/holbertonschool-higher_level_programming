#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for files in matrix:
        count = 0
        for column in files:
            count = count + 1
            print("{:d}".format(column), end="")
            if count != len(files):
                print(" ", end="")
        print("")
