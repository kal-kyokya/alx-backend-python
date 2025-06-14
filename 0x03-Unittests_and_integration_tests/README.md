# Unittests and Integration Tests

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.
<br />
The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?
<br />
Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.
<br />
Integration tests will test interactions between every part of the code.
<br />
Executing tests is done with:
```
$ python -m unittest path/to/test_file.py
```

## Learning Objectives

At the end of this project, I expect to be able to explain to anyone, without the help of Google:

- The difference between ```unit``` and ```integration tests```.
- Common testing patterns such as ```mocking```, ```parametrizations``` and ```fixtures```.

## Requirements
```
	->	All files will be interpreted/compiled on:
			Ubuntu 20+ LTS
				Using:
					python3 (version 3.9+)
	->	All files should end with a new line
	->	The first line of all files should be exactly:
			#!/usr/bin/env python3
	->	A README.md file, at the root of the folder of the project
	->	The code should use:
			The pycodestyle style (version 2.5)
	->	All files must be executable
	->	All modules should have a documentation:
			python3 -c 'print(__import__("my_module").__doc__)'
	->	All classes should have a documentation:
			python3 -c 'print(__import__("my_module").MyClass.__doc__)'
	->	All functions (inside and outside a class) should have a documentation:
			python3 -c 'print(__import__("my_module").my_function.__doc__)'
			python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
	->	A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method
	->	All functions and coroutines must be type-annotated.
```