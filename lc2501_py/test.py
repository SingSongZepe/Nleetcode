import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().longestSquareStreak(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [4,3,6,16,8,2]
        expected = 3
        self.t(nums, expected)

    def test2(self):
        nums = [2, 3, 5, 6, 7]
        expected = -1
        self.t(nums, expected)


if __name__ == '__main__':
    unittest.main()