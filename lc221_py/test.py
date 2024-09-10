import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maximalSquare(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().maximalSquare(arg)
        print(result)
        self.assertEqual(result, expected)

    def t3(self, arg, expected=None):
        result = Solution3().maximalSquare(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        matrix = [["1", "0", "1", "0", "0"],
                  ["1", "0", "1", "1", "1"],
                  ["1", "1", "1", "1", "1"],
                  ["1", "0", "0", "1", "0"]]
        expected = 4
        self.t(matrix, expected)

    def test2(self):
        matrix = [["0", "1"], ["1", "0"]]
        expected = 1
        self.t(matrix, expected)

    def test3(self):
        matrix = [["0"]]
        expected = 0
        self.t(matrix, expected)

    def test11(self):
        matrix = [["1", "0", "1", "0", "0"],
                  ["1", "0", "1", "1", "1"],
                  ["1", "1", "1", "1", "1"],
                  ["1", "0", "0", "1", "0"]]
        expected = 4
        self.t1(matrix, expected)

    def test21(self):
        matrix = [["0", "1"], ["1", "0"]]
        expected = 1
        self.t1(matrix, expected)

    def test31(self):
        matrix = [["0"]]
        expected = 0
        self.t1(matrix, expected)

    def test13(self):
        matrix = [["1", "0", "1", "0", "0"],
                  ["1", "0", "1", "1", "1"],
                  ["1", "1", "1", "1", "1"],
                  ["1", "0", "0", "1", "0"]]
        expected = 4
        self.t3(matrix, expected)

    def test23(self):
        matrix = [["0", "1"], ["1", "0"]]
        expected = 1
        self.t3(matrix, expected)

    def test33(self):
        matrix = [["0"]]
        expected = 0
        self.t3(matrix, expected)

if __name__ == '__main__':
    unittest.main()