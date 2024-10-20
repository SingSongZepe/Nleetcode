import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, index, expected=None):
        result = Solution().createTargetArray(nums, index)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, nums, index, expected=None):
        result = Solution1().createTargetArray(nums, index)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [0, 1, 2, 3, 4]
        index = [0, 1, 2, 2, 1]
        expected = [0, 4, 1, 3, 2]
        self.t(nums, index, expected)

    def test2(self):
        nums = [1, 2, 3, 4, 0]
        index = [0, 1, 2, 3, 0]
        expected = [0, 1, 2, 3, 4]
        self.t(nums, index, expected)

    def test3(self):
        nums = [1]
        index = [0]
        expected = [1]
        self.t(nums, index, expected)

    def test11(self):
        nums = [0, 1, 2, 3, 4]
        index = [0, 1, 2, 2, 1]
        expected = [0, 4, 1, 3, 2]
        self.t1(nums, index, expected)

    def test21(self):
        nums = [1, 2, 3, 4, 0]
        index = [0, 1, 2, 3, 0]
        expected = [0, 1, 2, 3, 4]
        self.t1(nums, index, expected)

    def test31(self):
        nums = [1]
        index = [0]
        expected = [1]
        self.t1(nums, index, expected)


if __name__ == '__main__':
    unittest.main()