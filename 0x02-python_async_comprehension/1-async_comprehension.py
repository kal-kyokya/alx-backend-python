#!/usr/bin/env python3
"""
'1-async_comprehension' creates a coroutine that processes an async generator
"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Creates a list comprehension off of an async generator"""
    return ([generated async for generated in async_generator()])
