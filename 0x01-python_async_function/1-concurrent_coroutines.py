#!/usr/bin/env python3
"""
'1-concurrent_coroutines' uses nested coroutines to create async calls layers
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn an async function a user defined number of times."""
    return (sorted(
        await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    ))
