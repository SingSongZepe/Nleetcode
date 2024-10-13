import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().finalPrices(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().finalPrices(arg)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        prices = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.t(prices, expected)

    def test2(self):
        prices = [10, 1, 1, 6]
        expected = [9, 0, 1, 6]
        self.t(prices, expected)

    def test3(self):
        prices = [8, 4, 6, 2, 3]
        expected = [4, 2, 4, 2, 3]
        self.t(prices, expected)

    def test11(self):
        prices = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.t1(prices, expected)

    def test21(self):
        prices = [10, 1, 1, 6]
        expected = [9, 0, 1, 6]
        self.t1(prices, expected)

    def test31(self):
        prices = [8, 4, 6, 2, 3]
        expected = [4, 2, 4, 2, 3]
        self.t1(prices, expected)


if __name__ == '__main__':
    unittest.main()