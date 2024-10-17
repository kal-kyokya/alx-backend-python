#!/usr/bin/env python3
"""
'100-safe_first_element' duck type annotates the code below
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]

    return None
