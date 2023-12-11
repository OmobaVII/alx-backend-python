#!/usr/bin/env python3
"""
    This module provides a function that zooms in on a tuple.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    This function takes a tuple and a zoom factor, and returns a new list
    with the elements of the tuple repeated according to the zoom factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in

    array = (12, 72, 91)

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3)
