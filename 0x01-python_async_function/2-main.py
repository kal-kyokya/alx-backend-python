#!/usr/bin/env python3
"""
'2-main' is a test file for a coroutine's correct output
"""
import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime

print(asyncio.run(measure_runtime(8, 0)))
print(asyncio.run(measure_runtime(4, 8)))
print(asyncio.run(measure_runtime(1, 4)))
print(f"{asyncio.run(measure_runtime(8, 0)): .02f}")
