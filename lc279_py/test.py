import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().numSquares(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().numSquares(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 12
        expected = 3
        self.t(n, expected)

    def test2(self):
        n = 13
        expected = 2
        self.t(n, expected)


    def test11(self):
        n = 12
        expected = 3
        self.t1(n, expected)

    def test21(self):
        n = 13
        expected = 2
        self.t1(n, expected)

    def test31(self):
        n = 9999
        expected = 31
        self.t1(n, expected)

if __name__ == '__main__':
    unittest.main()