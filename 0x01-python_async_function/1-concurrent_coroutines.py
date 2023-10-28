#!/usr/bin/env python3
"""
This module imports max_delay from the previous module
and provides an async routine called wait_n that takes
2 arguments max_delay and n
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """implements multiple coroutines at thesame time with async"""
    delay: List[float] = []
    delays: List[float] = []
    for a in range(n):
        delay.append(wait_random(max_delay))
    for b in asyncio.as_completed(delay):
        first_result = await b
        delays.append(first_result)
    return delays
