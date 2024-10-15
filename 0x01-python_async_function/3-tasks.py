#!/usr/bin/env python3
"""
'3-tasks' creates an async task using  a python function.
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Run an async coroutine as a task."""
    return (asyncio.create_task(wait_random(max_delay)))
