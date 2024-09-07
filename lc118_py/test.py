import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().generate(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().generate(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        numRows = 5
        expected = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        self.t(numRows, expected)

    def test2(self):
        numRows = 1
        expected = [[1]]
        self.t(numRows, expected)

    def test11(self):
        numRows = 5
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.t1(numRows, expected)

    def test21(self):
        numRows = 1
        expected = [[1]]
        self.t1(numRows, expected)

if __name__ == '__main__':
    unittest.main()