import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().runningSum(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1, 2, 3, 4]
        expected = [1, 3, 6, 10]
        self.t(nums, expected)

    def test2(self):
        nums = [1, 1, 1, 1, 1]
        expected = [1, 2, 3, 4, 5]
        self.t(nums, expected)

    def test3(self):
        nums = [3, 1, 2, 10, 1]
        expected = [3, 4, 6, 16, 17]
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()