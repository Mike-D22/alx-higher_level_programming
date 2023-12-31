#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elemts of a list that are int.

    Args:
        my_list (list): The list to print elmnts from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for z in range(0, x):
        try:
            print("{:d}".format(my_list[z]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
