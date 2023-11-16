#!/usr/bin/env python3
""" module that provides measure_time function """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time for wait_n(n, max_delay) """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()
    time_taken = stop_time - start_time
    average_time = time_taken / n
    return average_time
