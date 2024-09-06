import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, grid, k, expected=None):
        result = Solution().shiftGrid(grid, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        grid = [[1,2,3],[4,5,6],[7,8,9]]
        k = 1
        expected = [[9,1,2],[3,4,5],[6,7,8]]
        self.t(grid, k, expected)

    def test2(self):
        grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
        k = 4
        expected = [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
        self.t(grid, k, expected)

    def test3(self):
        grid = [[1,2,3],[4,5,6],[7,8,9]]
        k = 9
        expected = [[1,2,3],[4,5,6],[7,8,9]]
        self.t(grid, k, expected)

if __name__ == '__main__':
    unittest.main()