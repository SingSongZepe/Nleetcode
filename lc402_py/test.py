import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, num, k, expected=None):
        result = Solution().removeKdigits(num, k)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        num = '1432219'
        k = 3
        expected = '1219'
        self.t(num, k, expected)

    def test2(self):
        num = '10200'
        k = 1
        expected = '200'
        self.t(num, k, expected)

    def test3(self):
        num = '10'
        k = 2
        expected = '0'
        self.t(num, k, expected)

if __name__ == '__main__':
    unittest.main()