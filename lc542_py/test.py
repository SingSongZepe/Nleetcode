import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().updateMatrix(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().updateMatrix(arg)
        print(result)
        self.assertEqual(result, expected)

    def t2(self, arg, expected=None):
        result = Solution2().updateMatrix(arg)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.t(mat, expected)

    def test2(self):
        mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        self.t(mat, expected)

    def test12(self):
        mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.t2(mat, expected)

    def test22(self):
        mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        self.t2(mat, expected)

if __name__ == '__main__':
    unittest.main()