#!/usr/bin/env python3
"""
'8-make_multiplier' creates a function whose return is yet another function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function multiplying a float by the input number"""
    def multiply(num: float) -> float:
        """Inner function doing the aformentioned multiplication."""
        return (num * multiplier)
    return (multiply)
