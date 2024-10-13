import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, n, expected=None):
        result = Solution().shuffle(nums, n)
        print(result)
        self.assertEqual(result, expected)

    def t2(self, nums, n, expected=None):
        result = Solution2().shuffle(nums, n)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [2, 5, 1, 3, 4, 7]
        n = 3
        expected = [2, 3, 5, 4, 1, 7]
        self.t(nums, n, expected)

    def test2(self):
        nums = [1, 2, 3, 4, 4, 3, 2, 1]
        n = 4
        expected = [1, 4, 2, 3, 3, 2, 4, 1]
        self.t(nums, n, expected)

    def test3(self):
        nums = [1, 1, 2, 2]
        n = 2
        expected = [1, 2, 1, 2]
        self.t(nums, n, expected)

    def test12(self):
        nums = [1, 2, -1, -2]
        n = 2
        expected = [1, -1, 2, -2]
        self.t2(nums, n, expected)

    def test22(self):
        nums = [1, 2, 3, -1, -2, -3]
        n = 3
        expected = [1, -1, 2, -2, 3, -3]
        self.t2(nums, n, expected)

    def test32(self):
        nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
        n = 5
        expected = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
        self.t2(nums, n, expected)

    def test42(self):
        nums = [1, 2, 3, 4, -1, -2, -3, -4]
        n = 4
        expected = [1, -1, 2, -2, 3, -3, 4, -4]
        self.t2(nums, n, expected)


if __name__ == '__main__':
    unittest.main()