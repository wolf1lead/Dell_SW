#!/usr/bin/env python
#
# This Python file uses the following encoding: utf-8
""" docstring

This module is the unittest for challenge.py.

Usage: pytest test_challenge.py

"""
import unittest
from challenge import check_file

class C1TestCase(unittest.TestCase):
    """Tests for challenge.py."""

    def test_file_exist(self):
        """Does the file exist?"""
        self.assertTrue(check_file('words.txt'))

    def test_file_has_contents(self):
        """Does the file have contents"""
        self.assertTrue(check_file('word.txt'), msg='empty file')

    def test_file_is_a_directory(self):
        """Is the file a directory"""
        self.assertTrue(check_file('boo'), msg='is a directory')

if __name__ == '__main__':
    unittest.main()
