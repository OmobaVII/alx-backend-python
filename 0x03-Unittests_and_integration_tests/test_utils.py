#!/usr/bin/env python3
""" Provides test cases for for the functions in the utils module """
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Testcase for the Access_nested_map function """
    """ decorator to test the function for following inputs """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_return):
        """ method to test that the method returns the expected return """
        self.assertEqual(access_nested_map(nested_map, path), expected_return)
