import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().longestSubarray(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1, 2, 3, 3, 2, 2]
        expected = 2
        self.t(nums, expected)

    def test2(self):
        nums = [1, 2, 3, 4]
        expected = 1
        self.t(nums, expected)

    def test3(self):
        nums = [311155,311155,311155,311155,311155,311155,311155,311155,201191,311155]
        expected = 8
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()