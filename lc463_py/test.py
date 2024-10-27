import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().islandPerimeter(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        expected = 16
        self.t(grid, expected)

    def test2(self):
        grid = [[1]]
        expected = 4
        self.t(grid, expected)

    def test3(self):
        grid = [[1, 0]]
        expected = 4
        self.t(grid, expected)

if __name__ == '__main__':
    unittest.main()