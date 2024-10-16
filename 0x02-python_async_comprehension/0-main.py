#!/usr/bin/env python3
"""
'0-main' is a test file for correct output of an asynchronous generator
"""
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
