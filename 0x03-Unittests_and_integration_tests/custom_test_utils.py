#!/usr/bin/env python3
"""
'test_utils' defines a test method for a test class meant to assert the return values of calls made to 'utils.access_nested_map'
"""
import utils
import unittest
from parameterized import parameterized
from unittest.mock import patch


access = utils.access_nested_map
g_js = utils.get_json


class TestAccessNestedMap(unittest.TestCase):
    """A collection of methods testing the 'access_nested_map' built-in function.
    Inheritance:
    	unittest.TestCase: Class defining assertion functions required for actual testing.
    """

    @parameterized.expand(
        [
            (
                "me",
                {
                    "human": {
                        "african": {
                            "congolese": {
                                "name": "Jean-Paul De Marie KYOKYA KALULU",
                            }
                        }
                    }
                },
                ("human", "african", "congolese", "name"),
                "Jean-Paul De Marie KYOKYA KALULU"
            ),
            (
                "age",
                {
                    "human": {
                        "african": {
                            "congolese": {
                                "name": "Jean-Paul De Marie KYOKYA KALULU",
                                "age": 72,
                            }
                        }
                    }
                },
                ("human", "african", "congolese", "age"),
                72
            ),
            (
                "belief",
                {
                    "human": {
                        "african": {
                            "congolese": {
                                "name": "Jean-Paul De Marie KYOKYA KALULU",
                                "age": 72,
                                "belief": "truth",
                            }
                        }
                    }
                },
                ("human", "african", "congolese", "belief"),
                "truth"
            ),
            (
                "value",
                {
                    "human": {
                        "african": {
                            "congolese": {
                                "name": "Jean-Paul De Marie KYOKYA KALULU",
                                "age": 72,
                                "belief": "truth",
                                "value": "inner-peace",
                            }
                        }
                    }
                },
                ("human", "african", "congolese", "value"),
                "inner-peace"
            ),
            (
                "worldview",
                {
                    "human": {
                        "african": {
                            "congolese": {
                                "name": "Jean-Paul De Marie KYOKYA KALULU",
                                "age": 72,
                                "belief": "truth",
                                "value": "inner-peace",
                                "worldview": "Chaos & Order",
                            }
                        }
                    }
                },
                ("human", "african", "congolese", "worldview"),
                "Chaos & Order"
            ),
        ]
    )
    def test_access_nested_map(self, name, nested_map, path, expected):
        """Test method asserting the return value of 'utils.access_nested_method'
        Args:
        	self: Object in which all inherited methods, properties and attributes are stored
        	name: Assigns the parameterized test case a unique name
        	nested_map: The dictionary to be traversed by 'utils.access_nested_map'
        	path: A tuple guiding traversal of the dictionary
        	expected: The correct return value upon traversal
        Return:
        	Raises an 'Exception' if the test fails, None otherwise
        """
        self.assertEqual(access(nested_map, path), expected)

    @parameterized.expand(
        [
            (
                "me",
                {
                    "human": {
                        "african": {
                            "congolese": {
                                "name": "Jean-Paul De Marie KYOKYA KALULU",
                            }
                        }
                    }
                },
                ("human", "african", "congolese", "name"),
                "Jean-Paul De Marie KYOKYA kalulu"
            ),
            (
                "age",
                {
                    "human": {
                        "african": {
                            "congolese": {
                                "name": "Jean-Paul De Marie KYOKYA KALULU",
                                "age": 72,
                            }
                        }
                    }
                },
                ("human", "african", "congolese", "age"),
                1972
            ),
            (
                "belief",
                {
                    "human": {
                        "african": {
                            "congolese": {
                                "name": "Jean-Paul De Marie KYOKYA KALULU",
                                "age": 72,
                                "belief": "truth",
                            }
                        }
                    }
                },
                ("human", "african", "congolese", "belief"),
                "Truth"
            ),
            (
                "value",
                {
                    "human": {
                        "african": {
                            "congolese": {
                                "name": "Jean-Paul De Marie KYOKYA KALULU",
                                "age": 72,
                                "belief": "truth",
                                "value": "inner-peace",
                            }
                        }
                    }
                },
                ("human", "african", "congolese", "value"),
                "Inner-peace"
            ),
            (
                "worldview",
                {
                    "human": {
                        "african": {
                            "congolese": {
                                "name": "Jean-Paul De Marie KYOKYA KALULU",
                                "age": 72,
                                "belief": "truth",
                                "value": "inner-peace",
                                "worldview": "Chaos & Order",
                            }
                        }
                    }
                },
                ("human", "african", "congolese", "worldview"),
                "Chaos & order"
            ),
        ]
    )
    def test_access_nested_map_exception(self, name, nested_map, path, expected):
        """Test method asserting the return value of 'utils.access_nested_method'
        Args:
        	self: Object in which all inherited methods, properties and attributes are stored
        	nested_map: The dictionary to be traversed by 'utils.access_nested_map'
        	path: A tuple guiding traversal of the dictionary
        Return:
        	Raises an 'Exception' if the test fails, None otherwise
        """
        with self.assertRaises(AssertionError):
            self.assertEqual(access(nested_map, path), expected)


class TestGetJson(unittest.TestCase):
    """A collection of methods testing the functioning of the 'get_json' built-in function.
    Inheritance:
    	unittest.TestCase: Class defining assertion functions required for actual testing.
    """

    @parameterized.expand([
        (
            "futtech",
            "https://jsonplaceholder.typicode.com/comments/1",
            {'postId': 1, 'id': 1, 'name': 'id labore ex et quam laborum', 'email': 'Eliseo@gardner.biz', 'body': 'laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium'}
        ),
        (
            "eviot",
            "https://jsonplaceholder.typicode.com/users/1",
            {'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}
        ),
    ])
    @patch('requests.get')
    def test_get_json(self, name, url, payload, mock_get):
        """Ensure that 'utils.get_json' returns the expected value
        Args:
        	self: Object storing all 'unittest.TestCase' inherited methods
        Return:
        	Raises an AssertionError if test fails, None otherwise
        """
        mock_get.return_value.json.return_value = payload

        self.assertEqual(g_js(url), payload)
