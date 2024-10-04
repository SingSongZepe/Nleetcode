import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, p, expected=None):
        result = Solution().minSubarray(nums, p)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [3, 1, 4, 2]
        p = 6
        expected = 1
        self.t(nums, p, expected)

    def test2(self):
        nums = [6, 3, 5, 2]
        p = 9
        expected = 2
        self.t(nums, p, expected)

    def test3(self):
        nums = [1, 2, 3]
        p = 3
        expected = 0
        self.t(nums, p, expected)

    def test4(self):
        nums = [1, 2, 3]
        p = 7
        expected = -1
        self.t(nums, p, expected)

if __name__ == '__main__':
    unittest.main()