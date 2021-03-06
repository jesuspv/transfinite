# implementations of algorithms to support 
# the ordinal classes and their arithmetic

from functools import reduce
import operator

def hi_lo_bisect_right(lst, x):
    """
    bisect list sorted high -> low. Based on the code in:
    https://hg.python.org/cpython/file/3.4/Lib/bisect.py
    """
    hi, lo = 0, len(lst)
    while hi < lo:
        mid = (lo + hi) // 2
        if x > lst[mid]:
            lo = mid
        else:
            hi = mid + 1
    return hi

def product(terms):
    """
    return the product of the terms in a sequence
    """
    return reduce(operator.mul, terms)

