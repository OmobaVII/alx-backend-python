#!/usr/bin/env python3
"""
    This module provides a function that sums list of different types.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function computes the sum of a list of integers and floats
    """
    return sum(mxd_lst)
