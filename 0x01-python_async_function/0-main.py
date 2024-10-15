#!/usr/bin/env python3
"""
'0-main' is a coroutine test file for printing the correct output
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(10)))
print(asyncio.run(wait_random(15)))
