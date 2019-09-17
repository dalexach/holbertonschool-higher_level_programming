#!/usr/bin/python3


def no_c(my_string):
    str_list = list(my_string)
    try:
        str_list.remove('c')
    except ValueError:
        pass
    try:
        str_list.remove('C')
    except ValueError:
        pass
    my_string = ''.join(str_list)
    return my_string
