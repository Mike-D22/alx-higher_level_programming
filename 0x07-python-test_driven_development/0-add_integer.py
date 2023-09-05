#!/usr/bin/python3
# 0-add_integer.py
"""
Defines an int addition fun.
"""


def add_integer(a, b=98):
    """Returns the int addition of a and b.

    Float argumnts are typecasted to int's before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
