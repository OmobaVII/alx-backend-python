#!/usr/bin/env python3
"""
This module tests the access_nested_map function
in the utils module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """tests"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_accessnestedmap(self, nested_map, path, expected_result):
        """test for access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
