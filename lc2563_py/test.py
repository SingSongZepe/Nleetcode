import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, lower, upper, expected=None):
        result = Solution().countFairPairs(nums, lower, upper)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [0, 1, 7, 4, 4, 5]
        lower = 3
        upper = 6
        expected = 6
        self.t(nums, lower, upper, expected)

    def test2(self):
        nums = [1,7,9,2,5]
        lower = 11
        upper = 11
        expected = 1
        self.t(nums, lower, upper, expected)


if __name__ == '__main__':
    unittest.main()