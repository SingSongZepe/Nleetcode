import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().stoneGame(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        piles = [5, 3, 4, 5]
        expected = True
        self.t(piles, expected)

    def test2(self):
        piles = [3, 7, 2, 3]
        expected = True
        self.t(piles, expected)

if __name__ == '__main__':
    unittest.main()