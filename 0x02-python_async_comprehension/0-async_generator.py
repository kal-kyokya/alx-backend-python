#!/usr/bin/env python3
"""
'0-async_generator' defines a function to be used as integer generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """Generates 10 random number between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
