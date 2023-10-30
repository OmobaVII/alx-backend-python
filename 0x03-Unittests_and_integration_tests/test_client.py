#!/usr/bin/env python3
""" Tests for the client module"""
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized
from client import GithubOrgClient
import client
from utils import memoize


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

    def test_public_repos_url(self):
        """ test the _public_repos_url function of client """
        output = "www.yes.com"
        payload = {"repos_url": output}
        mock = 'client.GithubOrgClient.org'
        with patch(mock, PropertyMock(return_value=payload)):
            r = GithubOrgClient("x")
            self.assertEqual(r._public_repos_url, output)

    @patch('client.get_json')
    def test_public_repos(self, get_jsonmock):
        """ test the public repos function in client """
        omoba = {"name": "Omoba", "license": {"key": "a"}}
        sanni = {"name": "Sanni", "license": {"key": "b"}}
        betty = {"name": "Betty"}
        mock = 'client.GithubOrgClient._public_repos_url'
        get_jsonmock.return_value = [omoba, sanni, betty]
        with patch(mock, PropertyMock(return_value="www.yes.com")) as yes:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ['Omoba', 'Sanni', 'Betty'])
            self.assertEqual(x.public_repos("a"), ['Omoba'])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos(45), [])
            get_jsonmock.assert_called_once_with("www.yes.com")
            yes.assert_called_once_with()
