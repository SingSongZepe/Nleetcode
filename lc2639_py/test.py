import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().findColumnWidth(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        grid = [[1], [22], [333]]
        expected = [3]
        self.t(grid, expected)

    def test2(self):
        grid = [[-15,1,3],[15,7,12],[5,6,-2]]
        expected = [3, 1, 2]
        self.t(grid, expected)

    def test_count_len(self):
        print(count_len(-10))
        print(count_len(10))
        print(count_len(0))
        print(count_len(100))
        print(count_len(-100))



if __name__ == '__main__':
    unittest.main()