#!/usr/bin/python3
def read_file(filename=""):
    """ Function that read a text file (UTF8) and prints it stdout """
    with open(filename, encoding='utf-8') as f:
        read_file = f.read()
    print('{:s}'.format(read_file), end="")
