import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().nextGreaterElements(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1, 2, 1]
        expected = [2, -1, 2]
        self.t(nums, expected)

    def test2(self):
        nums = [1, 2, 3, 4, 3]
        expected = [2, 3, 4, -1, 4]
        self.t(nums, expected)

    def test3(self):
        nums = [5, 4, 3, 2, 1]
        expected = [-1, 5, 5, 5, 5]
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()