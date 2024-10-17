#!/usr/bin/env python3

safely_get_value = __import__('101-safely_get_value').safely_get_value
annotations = safely_get_value.__annotations__

print("Here's what the mappings should look like")
for k, v in annotations.items():
    print(("{}: {}".format(k, v)))

print(safely_get_value({1: 'a', 2: 'b', 3: 'c'}, 3, "No"))
print(safely_get_value({'Ally': 'Mother',
                        'Dj Mère': 'Genitrice',
                        'Stella': 'La famille'}, 'Dem', 'Le sang'))
print(safely_get_value({}, 'Something', 'Nothing'))
