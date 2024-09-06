import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, piles, h, expected=None):
        result = Solution().minEatingSpeed(piles, h)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        piles = [3, 6, 7, 11]
        h = 8
        expected = 4
        self.t(piles, h, expected)

    def test2(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        expected = 30
        self.t(piles, h, expected)

    def test3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        expected = 23
        self.t(piles, h, expected)

if __name__ == '__main__':
    unittest.main()