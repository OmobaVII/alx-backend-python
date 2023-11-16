#!/usr/bin/env python3
"""
Modifies wait_n to task_wait_n
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """implements multiple coroutines at thesame time with async"""
    delay: List[float] = []
    delays: List[float] = []
    for a in range(n):
        delay.append(task_wait_random(max_delay))
    for b in asyncio.as_completed(delay):
        first_result = await b
        delays.append(first_result)
    return delays
