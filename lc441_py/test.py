import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().arrangeCoins(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 5
        expected = 2
        self.t(n, expected)

    def test2(self):
        n = 8
        expected = 3
        self.t(n, expected)

if __name__ == '__main__':
    unittest.main()