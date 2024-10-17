#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)
print(element_length([(1, 2), "Dem"]))
print(element_length([{1:'a', 2:'b', 4:'Dem'}, '798129095']))
