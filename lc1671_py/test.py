import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minimumMountainRemovals(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1, 3, 1]
        expected = 0
        self.t(nums, expected)

    def test2(self):
        nums = [2, 1, 1, 5, 6, 2, 3, 1]
        expected = 3
        self.t(nums, expected)

    def test3(self):
        nums = [9,8,1,7,6,5,4,3,2,1]
        expected = 2
        self.t(nums, expected)

    def test4(self):
        nums = [100,92,89,77,74,66,64,66,64]
        expected = 6
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()