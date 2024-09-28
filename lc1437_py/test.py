import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, k, expected=None):
        result = Solution().kLengthApart(nums, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1, 0, 0, 0, 1, 0, 0, 1]
        k = 2
        expected = True
        self.t(nums, k, expected)

    def test2(self):
        nums = [1, 0, 0, 1, 0, 1]
        k = 2
        expected = False
        self.t(nums, k, expected)

if __name__ == '__main__':
    unittest.main()