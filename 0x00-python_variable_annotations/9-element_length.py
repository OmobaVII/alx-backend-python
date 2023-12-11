#!/usr/bin/env python3
"""
    This module provides a function that finds the length of each
    element in a list of strings.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a list of strings and returns a list of tuples,
    """
    return [(i, len(i)) for i in lst]
