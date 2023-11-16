#!/usr/bin/env python3
""" this module has a function task_wait_random
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ creates a task """
    new_task = asyncio.create_task(wait_random(max_delay))
    return new_task
