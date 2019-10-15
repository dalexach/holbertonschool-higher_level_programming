#!/usr/bin/python3
"""
Add an attribute if it can
"""


def add_attribute(obj, aname, value):
    """ add attributes """
    if isinstance(obj, (bool, int, float, tuple, str, frozenset)):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, aname, value)
