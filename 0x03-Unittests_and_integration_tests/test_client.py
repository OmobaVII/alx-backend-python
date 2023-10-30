#!/usr/bin/env python3
""" Tests for the client module"""
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized
from client import GithubOrgClient
import client


class TestGithubOrgClient(unittest.TestCase):
    """ Test that json can be got """
    """ decorator to parametrize the test """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, output, getpatch):
        """ Test the org function of client """
        getpatch.return_value = output
        x = GithubOrgClient(org)
        self.assertEqual(x.org, output)
        getpatch.assert_called_once_with("https://api.github.com/orgs/"+org)
