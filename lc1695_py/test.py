import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maximumUniqueSubarray(arg)
        print(result)

    def test1(self):
        nums = [4, 2, 4, 5, 6]
        expected = 17
        self.t(nums, expected)

    def test2(self):
        nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
        expected = 8
        self.t(nums, expected)

    def test3(self):
        nums = [1000]
        expected = 1000
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()