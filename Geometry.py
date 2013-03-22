#!/usr/bin/python
# -*- coding: utf-8 -*-
import doctest
from math import sqrt
############################################


def length(a, b):
    """
    Returns the length between 2 points
    >>> length((1,0),(0,0))
    1.0
    """
    return sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))


############################################
def __common_side__(a, b):
    if (length(a[0], b[0]) + length(a[1], b[0]) == length(a[0], a[1])) and \
            (length(a[0], b[1]) + length(a[1], b[1]) == length(a[0], a[1])):
        return 1
    elif ((length(a[0], b[0]) + length(a[1], b[0]) == length(a[0], a[1])) and not
            (a[0] == b[0] or a[1] == b[0])) and \
            ((-(a[1][0] - a[0][0]) * (b[1][1] - a[0][1]) +
            (b[1][0] - a[0][0]) * (a[1][1] - a[0][1])) == 0):
        return 1
    elif (length(a[0], b[1]) + length(a[1], b[1]) == length(a[0], a[1])) and\
            (length(a[0], b[0]) + length(a[1], b[0]) == length(a[0], a[1])):
        return 1
    elif ((length(a[0], b[1]) + length(a[1], b[1]) == length(a[0], a[1])) and not
            (a[0] == b[1] or a[1] == b[1])) and\
            (-(a[1][0] - a[0][0]) * (b[0][1] - a[0][1]) +
            (b[0][0] - a[0][0]) * (a[1][1] - a[0][1]) == 0):
        return 1
    else:
        return 0


def common_side(a, b):
    return __common_side__(a, b) or __common_side__(b, a)


###########################################
def subcontract(a, b):
    """Returns 1 if 2 polygons are subcontract
        and 0 if NOT
    >>> subcontract( (((0,0),(0,1)),((0,1),(1,1)),((1,1),(1,0)),((1,0),(0,0))), \
    (((0,0),(0,1)),((0,1),(-1,1)),((-1,1),(-1,0)),((-1,0),(0,0))))
    1
    """
    for x in a:
        for y in b:
            if common_side(x, y):
                return 1
    return 0
