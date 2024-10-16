#!/usr/bin/env python3
"""
'1-main' is a test file for correct output of an async comprehension
"""
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())
