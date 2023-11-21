# -*- coding: utf-8 -*-
"""
Date: 2023/11/21
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Course: AP4063
Midterm: Question 4
Version: v0.1.0
"""

import sys
from os.path import join
from os.path import dirname
from os.path import abspath

project_root = join(
    dirname(abspath(__file__)),
    '..', 
)
sys.path.append(project_root)

import unittest
from q04_solved import multiply

class TestMultiply(unittest.TestCase):

    def test_multiply_1(self):
        self.assertEqual(multiply(10), 250)
    def test_multiply_2(self):
        self.assertEqual(multiply(5), 25)
    def test_multiply_3(self):
        self.assertEqual(multiply(200), 25000)
    def test_multiply_4(self):
        self.assertEqual(multiply(0), 0)
    def test_multiply_5(self):
        self.assertEqual(multiply(-2), -10)

if __name__ == '__main__':
    unittest.main()
