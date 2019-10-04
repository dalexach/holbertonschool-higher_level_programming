#!/usr/bin/python3
"""
Add Integer Module

This module takes two integers or/and float and adds them.
Otherwise raise a TypeError exception.
Floats must be casted into integers
"""


def add_integer(a, b=98):
    """
    Arguments:
    @a: First parameter
    @b: Second parameter, if is empty takes the value od 98

    Returns:
    An integer: a + b, otherwise raise a TypeError exception.

    Example:
    >>> add_integer(3, 2)
    5
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
