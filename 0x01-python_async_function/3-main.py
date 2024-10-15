#!/usr/bin/env python3
"""
'3-main' is a test file for correct output of an async coroutine
"""
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    "Test the imported function"
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
