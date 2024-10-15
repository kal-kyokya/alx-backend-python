#!/usr/bin/env python3
"""
'4-tasks' refactor task 1 function named wait_n through usage of a task
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn an async function a user defined number of times."""
    return (sorted(
        await asyncio.gather(*[task_wait_random(max_delay) for _ in range(n)])
    ))
