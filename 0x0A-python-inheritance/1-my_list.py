#!/usr/bin/python3
"""
Def an inherited list class MyList.
"""


class MyList(list):
    """
    Implementss sorted printing for the built-in list class.
    """

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
