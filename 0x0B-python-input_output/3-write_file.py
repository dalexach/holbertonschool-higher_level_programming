#!/usr/bin/python3
def write_file(filename="", text=""):
    """ Function that reads n lines of a text file (UTF8)
    and prints it to stdout """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
