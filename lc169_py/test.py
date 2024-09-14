import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().majorityElement(arg)
        print(result)
        self.assertEqual(result, expected)

    def t2(self, arg, expected=None):
        result = Solution2().majorityElement(arg)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        nums = [3,2,3]
        expected = 3
        self.t(nums, expected)

    def test2(self):
        nums = [2,2,1,1,1,2,2]
        expected = 2
        self.t(nums, expected)

    def test22(self):
        nums = [2,2,1,1,1,2,2]
        expected = 2
        self.t2(nums, expected)

if __name__ == '__main__':
    unittest.main()