import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().findMaximumScore(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1, 3, 1, 5]
        expected = 7
        self.t(nums, expected)

    def test2(self):
        nums = [4, 3, 1, 3, 2]
        expected = 16
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()