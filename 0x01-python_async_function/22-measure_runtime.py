#!/usr/bin/env python3
"""
'2-measure_runtime' computes the average time of nested coroutine calls
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_runtime(n: int, max_delay: int) -> float:
    """Calculates the average from a list of values."""
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return ((time.perf_counter() - start) / n)
