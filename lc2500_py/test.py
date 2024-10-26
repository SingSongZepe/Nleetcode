import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().deleteGreatestValue(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        grid = [[1,2,4],[3,3,1]]
        expected = 8
        self.t(grid, expected)

    def test2(self):
        grid = [[10]]
        expected = 10
        self.t(grid, expected)

if __name__ == '__main__':
    unittest.main()