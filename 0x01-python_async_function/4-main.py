#!/usr/bin/env python3
import asyncio


task_wait_n = __import__('4-tasks').task_wait_n

print(asyncio.run(task_wait_n(4, 8)))
print(asyncio.run(task_wait_n(1, 3)))
print(asyncio.run(task_wait_n(8, 0)))

