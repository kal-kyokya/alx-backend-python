#!/usr/bin/env python3
"""
'5-sum_list' Creates a function that reduces a list of float to a signle value
"""
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Reduces a list of floats into a single value"""
    return (reduce(lambda x, y: x + y, input_list))
