#!/usr/bin/python3
import sys
avg_age = __import__('4-stream_ages').avg_user_age


try:
    avg_age()
except Exception as err:
    print("Error: {}".format(err))
