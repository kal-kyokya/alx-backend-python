#!/usr/bin/env python3
"""
'test_utils' defines a suite of test classes for functions in module 'utils'
"""
import utils
import unittest
from parameterized import parameterized
from unittest.mock import patch


access = utils.access_nested_map
g_js = utils.get_json
memo = utils.memoize


class TestAccessNestedMap(unittest.TestCase):
    """A collection of methods testing 'utils.access_nested_map'
    Inheritance:
        unittest.TestCase: Class defining assertion functions needed for tests
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Asserts the return value of 'utils.access_nested_method'
        Args:
            self: Object in which all inherited methods, properties and
        attributes are stored
            nested_map: The dictionary to be traversed by
        'utils.access_nested_map'
            path: A tuple guiding traversal of the dictionary
            expected: The correct return value upon traversal
        Return:
            Raises an 'Exception' if the test fails, None otherwise
        """
        self.assertEqual(access(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Asserts the return value of 'utils.access_nested_method'
        Args:
            self: Object in which all inherited methods, properties and
        attributes are stored
            nested_map: The dictionary to be traversed by
        'utils.access_nested_map'
            path: A tuple guiding traversal of the dictionary
        Return:
            Raises an 'Exception' if the test fails, None otherwise
        """
        with self.assertRaises(KeyError):
            access(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A collection of methods testing 'utils.get_json'
    Inheritance:
        unittest.TestCase: Class defining assertion functions needed for tests
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("requests.get")
    def test_get_json(self, url, payload, mock_get):
        """Ensures that 'utils.get_json' returns an expected payload value
        Args:
            self: Object storing all 'unittest.TestCase' inherited methods
            name: String to be attached to parameterized tests
            url: String locating the desired web resource
            payload: The expected dictionary returned after the get request
            mock_get: The mock object replacing any call to 'requests.get'
        Return:
            Raises an AssertionError if test fails, None otherwise
        """
        mock_get.return_value.json.return_value = payload

        self.assertEqual(g_js(url), payload)


class TestMemoize(unittest.TestCase):
    """A collection of methods testing 'utils.memoize'
    Inheritance:
        unittest.TestCase: Class defining assertion functions needed for tests
    """

    class TestClass:

        def a_method(self):
            return 42

        @memo
        def a_property(self):
            return self.a_method()

    @patch("test_utils.TestMemoize.TestClass.a_method")
    def test_memoize(self, mock_method):
        """Ensures 'utils.memoize' prevents more than one call to 'a_method'
        Args:
            self: Object storing all 'unittest.TestCase' inherited methods
            mock_method: The mock object replacing any call to 'a_method'
        Return:
            Raises an AssertionError if test fails, None otherwise
        """
        test = self.TestClass()

        test.a_property()
        test.a_property()

        mock_method.assert_called_once()
