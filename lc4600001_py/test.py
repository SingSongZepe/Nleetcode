import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maximumMedianSum(arg)
        print(result)
        
    def test1(self):
        nums = [2, 1, 3, 2, 1, 3]
        expected = 5
        self.t(nums, expected)

    def test2(self):
        nums = [1, 1, 10, 10, 10, 10]
        expected = 20
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()