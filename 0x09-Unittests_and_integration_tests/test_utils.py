#!/usr/bin/env python3
'''Module toparameterize a unit test'''

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize, requests


class TestAccessNestedMap(unittest.TestCase):
    ''' Parameterize a unit test '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, map):
        '''test access for nested map'''
        self.assertEqual(access_nested_map(nested_map, path), map)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''' Test access nested map exception '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''test that utils.get_json returns the expected result.'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        '''Test get json'''
        my_mock = unittest.mock.Mock()
        my_mock.json.return_value = payload
        with patch('requests.get', return_value=my_mock):
            my_json = get_json(url)
            my_mock.json.assert_called_once()
            self.assertEqual(my_json, payload)


class TestMemoize(unittest.TestCase):
    '''Test for Memoize'''

    def test_memoize():
        '''Extrange method with class'''

        class TestClass:
            '''Test fortest class'''

            def a_method(self):
                '''return 42'''
                return 42

            @memoize
            def a_property(self):
                '''Return a method'''
                return self.a_method()

        with patch.object(TestClass, 'a_method') as my_mock:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            my_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
