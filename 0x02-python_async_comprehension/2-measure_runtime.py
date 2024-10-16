#!/usr/bin/env python3
"""
'2-measure_runtime' Computes the time taken by n async processes to run
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Computes the time taken by an async processes to complete"""
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return (time.perf_counter() - start)
