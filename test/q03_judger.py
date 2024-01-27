# -*- coding: utf-8 -*-
"""
Date: 2023/11/21
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Course: AP4063
Midterm: Question 3
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
from q03_solved import distances_from_average

class TestDistancesFromAverage(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            distances_from_average([55, 95, 62, 36, 48]), 
            [4.2, -35.8, -2.8, 23.2, 11.2]
        )

    def test_case_2(self):
        self.assertEqual(
            distances_from_average([1, 1, 1, 1, 1]), 
            [0, 0, 0, 0, 0]
        )

    def test_case_3(self):
        self.assertEqual(
            distances_from_average([1, -1, 1, -1, 1, -1]), 
            [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0]
        )

    def test_case_4(self):
        self.assertEqual(
            distances_from_average([1, -1, 1, -1, 1]), 
            [-0.8, 1.2, -0.8, 1.2, -0.8]
        )

    def test_case_5(self):
        self.assertEqual(
            distances_from_average([2, -2]), 
            [-2.0, 2.0]
        )

    def test_case_6(self):
        self.assertEqual(
            distances_from_average([1]), 
            [0]
        )

    def test_case_7(self):
        self.assertEqual(
            distances_from_average([123, -65, 32432, -353, -534]), 
            [6197.6, 6385.6, -26111.4, 6673.6, 6854.6]
        )

if __name__ == '__main__':
    unittest.main()
