import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minimumTotal(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        expected = 11
        self.t(triangle, expected)

    def test2(self):
        triangle = [[-10]]
        expected = -10
        self.t(triangle, expected)

if __name__ == '__main__':
    unittest.main()