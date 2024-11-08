import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, m, expected=None):
        result = Solution().getMaximumXor(nums, m)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [0, 1, 1, 3]
        maximumBit = 2
        expected = [0, 3, 2, 3]
        self.t(nums, maximumBit, expected)

    def test2(self):
        nums = [2, 3, 4, 7]
        maximumBit = 3
        expected = [5, 2, 6, 5]
        self.t(nums, maximumBit, expected)

    def test3(self):
        nums = [0, 1, 2, 2, 5, 7]
        maximumBit = 3
        expected = [4,3,6,4,6,7]
        self.t(nums, maximumBit, expected)



if __name__ == '__main__':
    unittest.main()