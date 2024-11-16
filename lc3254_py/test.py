import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, k, expected=None):
        result = Solution().resultsArray(nums, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1,2,3,4,3,2,5]
        k = 3
        expected = [3,4,-1,-1,-1]
        self.t(nums, k, expected)

    def test2(self):
        nums = [2, 2, 2, 2, 2]
        k = 4
        expected = [-1,-1]
        self.t(nums, k, expected)

    def test3(self):
        nums = [3, 2, 3, 2, 3, 2]
        k = 2
        expected = [-1,3,-1,3,-1]
        self.t(nums, k, expected)

if __name__ == '__main__':
    unittest.main()