#!/usr/bin/env python3
"""
This module tests the functions
in the utils module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """tests for the function access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """test for access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    """tests that key error is raised for the following inputs"""
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_accessnestedmap_invalid(self, nested_map, path):
        """test to see if a KeyError is raised"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """tests for the function get_json"""
    @parameterized.expand([
        ("http://google.com", {"payload": True}),
        ("http://omoba.tech", {"payload": False}),
    ])
    @unittest.mock.patch("test_utils.get_json")
    def test_getjson(self, test_url, payload, test_get):
        """test the function get_json returns expected"""
        test_get.return_value = payload
        r = get_json(test_url)
        self.assertEqual(r, payload)


class TestMemoize(unittest.TestCase):
    """test for the momoize"""
    def test_momoize(self):
        """test the memoize"""
        class TestMethod:
            """class for the methods"""
            def a_method(self):
                """the a_method test"""
                return 42

            @memoize
            def a_property(self):
                """the a_property test"""
                return self.a_method()
        with unittest.mock.patch.object(TestMethod, "a_method") as testmethod:
            test_method = TestMethod()
            test_method.a_property
            test_method.a_property
            testmethod.assert_called_once
