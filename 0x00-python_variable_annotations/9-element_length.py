#!/usr/bin/env python3
"""
'9-element_length' duck types an iterable object
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Models the 'len' built-in function."""
    return ([(i, len(i)) for i in lst])
