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
