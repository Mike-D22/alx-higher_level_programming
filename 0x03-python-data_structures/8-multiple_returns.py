#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """It returns the length of a strng and its 1st character"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
