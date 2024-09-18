import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().largestNumber(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [10, 2]
        expected = "210"
        self.t(nums, expected)

    def test2(self):
        nums = [3, 30, 34, 5, 9]
        expected = "9534330"
        self.t(nums, expected)


if __name__ == '__main__':
    unittest.main()