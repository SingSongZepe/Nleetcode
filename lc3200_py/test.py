import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, red, blue, expected=None):
        result = Solution().maxHeightOfTriangle(red, blue)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, red, blue, expected=None):
        result = Solution1().maxHeightOfTriangle(red, blue)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        red = 2
        blue = 4
        expected = 3
        self.t(red, blue, expected)

    def test2(self):
        red = 2
        blue = 1
        expected = 2
        self.t(red, blue, expected)

    def test3(self):
        red = 1
        blue = 1
        expected = 1
        self.t(red, blue, expected)

    def test4(self):
        red = 10
        blue = 1
        expected = 2
        self.t(red, blue, expected)

    def test11(self):
        red = 2
        blue = 4
        expected = 3
        self.t1(red, blue, expected)

    def test21(self):
        red = 2
        blue = 1
        expected = 2
        self.t1(red, blue, expected)

    def test31(self):
        red = 1
        blue = 1
        expected = 1
        self.t1(red, blue, expected)

    def test41(self):
        red = 10
        blue = 1
        expected = 2
        self.t1(red, blue, expected)

if __name__ == '__main__':
    unittest.main()