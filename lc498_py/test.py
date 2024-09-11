import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().findDiagonalOrder(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        mat = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [1,2,4,7,5,3,6,8,9]
        self.t(mat, expected)

    def test2(self):
        mat = [[1,2],[3,4]]
        expected = [1,2,3,4]
        self.t(mat, expected)

    def test3(self):
        mat = [[1]]
        expected = [1]
        self.t(mat, expected)

if __name__ == '__main__':
    unittest.main()