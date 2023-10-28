#!/usr/bin/env python3
"""
This module provide a function `wait_random`
this function shows the basic implementation
of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """an asynchronous coroutine that takes in an integer argument
    with a default of 10"""
    rand_float = random.uniform(0, max_delay)
    await asyncio.sleep(rand_float)
    return rand_float
