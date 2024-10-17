#!/usr/bin/env python3

zoom_array = __import__('102-type_checking').zoom_array

print(zoom_array.__annotations__)

array = [12, 72, 91]

zoom_2x = zoom_array(array)
print(zoom_2x)

zoom_3x = zoom_array(array, 3.0)
print(zoom_3x)
