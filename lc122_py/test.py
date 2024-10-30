import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maxProfit(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        prices = [7,1,5,3,6,4]
        expected = 7
        self.t(prices, expected)

    def test2(self):
        prices = [1,2,3,4,5]
        expected = 4
        self.t(prices, expected)

    def test3(self):
        prices = [7,6,4,3,1]
        expected = 0
        self.t(prices, expected)

    def test4(self):
        prices = [1, 2]
        expected = 1
        self.t(prices, expected)

    def test5(self):
        prices = [2,1,4,5,2,9,7]
        expected = 11
        self.t(prices, expected)

if __name__ == '__main__':
    unittest.main()