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
