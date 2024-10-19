import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, n, k, expected=None):
        result = Solution().findKthBit(n, k)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, n, k, expected=None):
        result = Solution1().findKthBit(n, k)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        n = 3
        k = 1
        expected = "0"
        self.t(n, k, expected)

    def test2(self):
        n = 4
        k = 11
        expected = "1"
        self.t(n, k, expected)

    def test11(self):
        n = 3
        k = 1
        expected = "0"
        self.t1(n, k, expected)

    def test21(self):
        n = 4
        k = 11
        expected = "1"
        self.t1(n, k, expected)

if __name__ == '__main__':
    unittest.main()