import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minGroups(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().minGroups(arg)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
        expected = 3
        self.t(intervals, expected)

    def test2(self):
        intervals = [[1,3],[5,6],[8,10],[11,13]]
        expected = 1
        self.t(intervals, expected)

    def test11(self):
        intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
        expected = 3
        self.t1(intervals, expected)

    def test21(self):
        intervals = [[1,3],[5,6],[8,10],[11,13]]
        expected = 1
        self.t1(intervals, expected)


if __name__ == '__main__':
    unittest.main()