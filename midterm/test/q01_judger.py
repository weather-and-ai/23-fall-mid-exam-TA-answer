# -*- coding: utf-8 -*-
"""
Date: 2023/11/21
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Course: AP4063
Midterm: Question 1
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
from q01_solved import four_piles

class TestFourPiles(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(four_piles(48, 3), [12, 6, 27, 3])

    def test_case_2(self):
        self.assertEqual(four_piles(100, 4), [20, 12, 64, 4])

    def test_case_3(self):
        self.assertEqual(four_piles(25, 4), [])

    def test_case_4(self):
        self.assertEqual(four_piles(24, 4), [])

if __name__ == '__main__':
    unittest.main()
