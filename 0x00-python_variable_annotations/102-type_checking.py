#!/usr/bin/env python3
"""
'102-type_checking' Validates a piece of code
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Replicates the elements of a tuple a user defined number of times"""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in
