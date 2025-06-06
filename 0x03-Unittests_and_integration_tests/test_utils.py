#!/usr/bin/env python3
"""
'test_utils' defines a test method for a test class meant to assert the return values of calls made to 'utils.access_nested_map'
"""
import utils
import unittest
from parameterized import parameterized


access = utils.access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A collection of methods aiming to test the functioning of a built-in function.
    Inheritance:
    	unittest.TestCase: Class defining assertion functions required for acutal testing.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test method asserting the return value of 'utils.access_nested_method'
        Args:
        	self: Object in which all inherited methods, properties and attributes are stored
        	nested_map: The dictionary to be traversed by 'utils.access_nested_map'
        	path: A tuple guiding traversal of the dictionary
        	expected: The correct return value upon traversal
        Return:
        	Raises an 'Exception' if the test fails, None otherwise
        """
        self.assertEqual(access(nested_map, path), expected)
