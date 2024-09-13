import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().constructRectangle(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        area = 4
        expected = [2, 2]
        self.t(area, expected)

    def test2(self):
        area = 37
        expected = [37, 1]
        self.t(area, expected)

    def test3(self):
        area = 122122
        expected = [427, 286]
        self.t(area, expected)


if __name__ == '__main__':
    unittest.main()