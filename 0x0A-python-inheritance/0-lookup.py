#!/usr/bin/python3
"""
Def an object attribute lookup funct.
"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
