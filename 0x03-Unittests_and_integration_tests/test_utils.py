#!/usr/bin/env python3

"""
Test suite for utils.py
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import (
    access_nested_map,
    memoize,
    get_json
    )


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for the utils..access_nested_map funtion
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, output):
        """
        Test method
        """
        self.assertEqual(access_nested_map(nested_map, path), output)
