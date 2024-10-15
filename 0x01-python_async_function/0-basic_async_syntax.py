#!/usr/bin/env python3
"""
'0-basic_async_syntax' creates a coroutine, sleeps for X seconds and then return X
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously sleeps for a random amount of seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return (delay)
