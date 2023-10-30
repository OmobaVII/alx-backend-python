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

    """ tests that keyerror is raised for the following inputs """
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test to see if a KeyError is raised """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ tests for the function get_json """
    """ decorator for function to test these inputs """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @unittest.mock.patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, test_get):
        """ test the function get_json returns expected """
        test_get.return_value = test_payload
        r = get_json(test_url)
        self.assertEqual(r, test_payload)
