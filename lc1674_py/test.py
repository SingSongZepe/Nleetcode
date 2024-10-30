import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, limit, expected=None):
        result = Solution().minMoves(nums, limit)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1, 2, 4, 3]
        limit = 4
        expected = 1
        self.t(nums, limit, expected)

    def test2(self):
        nums = [1, 2, 2, 1]
        limit = 2
        expected = 2
        self.t(nums, limit, expected)

    def test3(self):
        nums = [1, 2, 1, 2]
        limit = 2
        expected = 0
        self.t(nums, limit, expected)

if __name__ == '__main__':
    unittest.main()