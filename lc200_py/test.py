import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().numIslands(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        expected = 1
        self.t(grid, expected)

    def test2(self):
        grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        expected = 3
        self.t(grid, expected)

if __name__ == '__main__':
    unittest.main()