#!/usr/bin/env python3
"""
'6-sum_mixed_list' Creates a typed annotated function reducing a number list
"""
from functools import reduce
from typing import List


def sum_mixed_list(mxd_lst: List[int and float]) -> float:
    """Reduces a number list into a float number"""
    return (reduce(lambda x, y: x + y, mxd_lst))
