import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, k, expected=None):
        result = Solution().minimumSubarrayLength(nums, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1, 2, 1, 8]
        k = 10
        expected = 3
        self.t(nums, k, expected)

    def test2(self):
        nums = [1, 2]
        k = 0
        expected = 1
        self.t(nums, k, expected)

    def test3(self):
        nums = [1, 2, 3]
        k = 2
        expected = 1
        self.t(nums, k, expected)

    def test4(self):
        nums = [1, 2, 1, 8, 1, 10]
        k = 10
        expected = 1
        self.t(nums, k, expected)

    def test5(self):
        nums = [2,1,9,12]
        k = 21
        expected = -1
        self.t(nums, k, expected)


if __name__ == '__main__':
    unittest.main()