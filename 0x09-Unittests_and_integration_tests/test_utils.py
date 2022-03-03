#!/usr/bin/env python3
'''Module toparameterize a unit test'''

import unittest

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize, requests


class TestAccessNestedMap(unittest.TestCase):
    ''' Parameterize a unit test '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b")),
    ])
    def test_access_nested_map(self, nested_map, path, map):
        '''test access for nested map'''
        self.assertEqual(access_nested_map(nested_map, path), map)