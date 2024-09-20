import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().findMissingAndRepeatedValues(arg)
        print(result)
        self.t(arg, expected)
        
    def test1(self):
        grid = [[1, 3], [2, 2]]
        expected = [2, 4]
        self.t(grid, expected)

    def test2(self):
        grid = [[9,1,7],[8,9,2],[3,4,6]]
        expected = [9, 5]
        self.t(grid, expected)

    def test_find_repeating_and_missing(self):
        grid = [[1, 3], [2, 2]]
        expected = [2, 4]
        print(find_repeating_and_missing(grid))


if __name__ == '__main__':
    unittest.main()