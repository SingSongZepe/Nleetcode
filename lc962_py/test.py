import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maxWidthRamp(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [6,0,8,2,1,5]
        expected = 4
        self.t(nums, expected)

    def test2(self):
        nums = [9,8,1,0,1,9,4,0,4,1]
        expected = 7
        self.t(nums, expected)

    def test3(self):
        nums = [1, 2, 1]
        expected = 2
        self.t(nums, expected)


if __name__ == '__main__':
    unittest.main()