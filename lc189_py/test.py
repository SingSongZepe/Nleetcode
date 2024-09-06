import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, k, expected=None):
        Solution().rotate(nums, k)
        print(nums)
        self.assertEqual(nums, expected)
        
    def test1(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        expected = [5,6,7,1,2,3,4]
        self.t(nums, k, expected)

    def test2(self):
        nums = [-1,-100,3,99]
        k = 2
        expected = [3,99,-1,-100]
        self.t(nums, k, expected)

    def test3(self):
        nums = [-1]
        k = 2
        expected = [-1]
        self.t(nums, k, expected)

if __name__ == '__main__':
    unittest.main()