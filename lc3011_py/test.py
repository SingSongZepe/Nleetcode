import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().canSortArray(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [8, 4, 2, 30, 15]
        expected = True
        self.t(nums, expected)

    def test2(self):
        nums = [1, 2, 3, 4, 5]
        expected = True
        self.t(nums, expected)

    def test3(self):
        nums = [3,16,8,4,2]
        expected = False
        self.t(nums, expected)

    def test4(self):
        nums = [20, 16]
        expected = False
        self.t(nums, expected)

    def test5(self):
        nums = [1, 2]
        expected = True
        self.t(nums, expected)

    def test6(self):
        nums = [1]
        expected = True
        self.t(nums, expected)

    def test7(self):
        nums = [31,18,23]
        expected = False
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()