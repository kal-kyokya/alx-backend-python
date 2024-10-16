#!/usr/bin/env python3
"""
'7-to_kv' Creates a type annotated function and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """Return a tuple made of the string input and the square of the number"""
    return (tuple([k, v * v]))
