#!/usr/bin/env python3
"""
    This module provides a function that safely gets a value from
    a mapping.
i"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    This function gets the value for a given key in a mapping, or returns
    a default value if the key is not in the mapping.
    """
    if key in dct:
        return dct[key]
    else:
        return default
