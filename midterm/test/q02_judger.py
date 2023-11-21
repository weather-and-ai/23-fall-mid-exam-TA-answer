# -*- coding: utf-8 -*-
"""
Date: 2023/11/21
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Course: AP4063
Midterm: Question 2
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
from q02_solved import decode

class TestDecode(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            decode("sr"), 
            "hi"
        )

    def test_case_2(self):
        self.assertEqual(
            decode("svool"), 
            "hello"
        )

    def test_case_3(self):
        self.assertEqual(
            decode("r slkv mlylwb wvxlwvh gsrh nvhhztv"), 
            "i hope nobody decodes this message"
        )

    def test_case_4(self):
        self.assertEqual(
            decode("qzezxirkg rh z srts ovevo wbmznrx fmgbkvw zmw rmgvikivgvw kiltiznnrmt ozmtfztv rg szh yvvm hgzmwziwravw rm gsv vxnzxirkg ozmtfztv hkvxrurxzgrlm zolmthrwv sgno zmw xhh rg rh lmv lu gsv gsivv vhhvmgrzo gvxsmloltrvh lu dliow drwv dvy xlmgvmg kilwfxgrlm gsv nzqlirgb lu dvyhrgvh vnkolb rg zmw rg rh hfkkligvw yb zoo nlwvim dvy yildhvih drgslfg koftrmh"), 
            "javacript is a high level dynamic untyped and interpreted programming language it has been standardized in the ecmacript language specification alongside html and css it is one of the three essential technologies of world wide web content production the majority of websites employ it and it is supported by all modern web browsers without plugins"
        )

    def test_case_5(self):
        self.assertEqual(
            decode("gsv vrtsgs hbnkslmb dzh qvzm hryvorfh urmzo nzqli xlnklhrgrlmzo kilqvxg lxxfkbrmt srn rmgvinrggvmgob"), 
            "the eighth symphony was jean sibelius final major compositional project occupying him intermittently"
        )

    def test_case_6(self):
        self.assertEqual(
            decode("husbands ask repeated resolved but laughter debating"), 
            "sfhyzmwh zhp ivkvzgvw ivhloevw yfg ozftsgvi wvyzgrmt"
        )

    def test_case_7(self):
        self.assertEqual(
            decode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), 
            "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        )

    def test_case_8(self):
        self.assertEqual(
            decode(" "), 
            " "
        )

    def test_case_9(self):
        self.assertEqual(
            decode(""), 
            ""
        )

    def test_case_10(self):
        self.assertEqual(
            decode("thelastrandomsentence"), 
            "gsvozhgizmwlnhvmgvmxv"
        )

if __name__ == '__main__':
    unittest.main()