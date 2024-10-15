#!/usr/bin/env python3
"""
'2-main' is a test file for a coroutine's correct output
"""
measure_runtime = __import__('2-measure_runtime').measure_runtime


print(measure_runtime(8, 0))
print(measure_runtime(4, 8))
print(measure_runtime(1, 4))
print(f"{measure_runtime(8, 0): .10f}")
