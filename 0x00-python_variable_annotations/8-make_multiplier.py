#!/usr/bin/env python3
"""
This module provides a function that creates a function that
multiplies a float by a multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float as an argument and returns a function that
    multiplies a float by the multiplier.
    """

    def multiply(n: float) -> float:
        """
        This function multiplies a float by the multiplier.
        """
        return n * multiplier

    return multiply
