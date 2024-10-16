#!/usr/bin/env python3
"""
'2-main' tests for correct output a coroutine processing many async calls
"""
import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(asyncio.run(main()))
