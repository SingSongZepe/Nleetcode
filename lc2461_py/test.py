import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, k, expected=None):
        result = Solution().maximumSubarraySum(nums, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1, 5, 4, 2, 9, 9, 9]
        k = 3
        expected = 15
        self.t(nums, k, expected)

    def test2(self):
        nums = [4, 4, 4]
        k = 3
        expected = 0
        self.t(nums, k, expected)

    def test3(self):
        nums = [9,9,9,1,2,3]
        k = 3
        expected = 12
        self.t(nums, k, expected)


if __name__ == '__main__':
    unittest.main()