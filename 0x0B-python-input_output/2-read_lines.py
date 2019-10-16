#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ Function that reads n lines of a text file (UTF8)
    and prints it to stdout """
    counter = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if (counter < nb_lines) or (nb_lines == 0) or nb_lines < 0:
                print(line, end="")
            counter += 1
