import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().getMaxLen(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().getMaxLen(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1, -2, -3, 4]
        expected = 4
        self.t(nums, expected)

    def test2(self):
        nums = [0, 1, -2, -3, -4]
        expected = 3
        self.t(nums, expected)

    def test3(self):
        nums = [-1, -2, -3, 0, 1]
        expected = 2
        self.t(nums, expected)

    def test11(self):
        nums = [1, -2, -3, 4]
        expected = 4
        self.t1(nums, expected)

    def test21(self):
        nums = [0, 1, -2, -3, -4]
        expected = 3
        self.t1(nums, expected)

    def test31(self):
        nums = [-1, -2, -3, 0, 1]
        expected = 2
        self.t1(nums, expected)


if __name__ == '__main__':
    unittest.main()