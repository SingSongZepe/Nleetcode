import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maxSum(arg)
        self.assertEqual(result, expected)
        print(result)
        
    def test1(self):
        nums = [1, 1, 0, 1, 1]
        expected = 1
        self.t(nums, expected)

    def test2(self):
        nums = [-100]
        expected = -100
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()