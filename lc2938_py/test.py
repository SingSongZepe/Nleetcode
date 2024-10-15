import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minimumSteps(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().minimumSteps(arg)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        s = '101'
        expected = 1
        self.t(s, expected)

    def test2(self):
        s = '100'
        expected = 2
        self.t(s, expected)

    def test3(self):
        s = '0111'
        expected = 0
        self.t(s, expected)

    def test4(self):
        s = '0'
        expected = 0
        self.t(s, expected)

    def test11(self):
        s = '101'
        expected = 1
        self.t1(s, expected)

    def test21(self):
        s = '100'
        expected = 2
        self.t1(s, expected)

    def test31(self):
        s = '0111'
        expected = 0
        self.t1(s, expected)

    def test41(self):
        s = '0'
        expected = 0
        self.t1(s, expected)

if __name__ == '__main__':
    unittest.main()