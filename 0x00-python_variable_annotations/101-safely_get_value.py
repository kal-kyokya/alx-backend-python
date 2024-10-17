#!/usr/bin/env python3
"""
'101-safely_get_value' Use TypeVar to annotate a function made generic
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns an Object if a key input is in the dictionary. Otherwise None"""
    if key in dct:
        return (dct[key])

    return default
