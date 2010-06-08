# -*- coding: utf-8 -*-
#
# Copyright (c) The PyAMF Project.
# See LICENSE.txt for details.

"""
Python compatibility values and helpers.
"""

import types

class_types = [type]
int_types = [int]
str_types = [str]

try:
    int_types.append(long)
except NameError:
    pass

try:
    str_types.append(unicode)
except NameError:
    pass

try:
    class_types.append(types.ClassType)
except:
    pass

int_types = tuple(int_types)
str_types = tuple(str_types)
class_types = tuple(class_types)

PosInf = 1e300000
NegInf = -1e300000
# we do this instead of float('nan') because windows throws a wobbler.
NaN = PosInf / PosInf


def isNaN(val):
    """
    @since: 0.5
    """
    return str(float(val)) == str(NaN)


def isPosInf(val):
    """
    @since: 0.5
    """
    return str(float(val)) == str(PosInf)


def isNegInf(val):
    """
    @since: 0.5
    """
    return str(float(val)) == str(NegInf)



def check_for_int(x):
    """
    This is a compatibility function that takes a C{float} and converts it to an
    C{int} if the values are equal.
    """
    try:
        y = int(x)
    except (OverflowError, ValueError):
        pass
    else:
        # There is no way in AMF0 to distinguish between integers and floats
        if x == x and y == x:
            return y

    return x