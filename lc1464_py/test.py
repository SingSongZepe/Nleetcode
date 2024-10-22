import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maxProduct(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [3, 4, 5, 2]
        expected = 12
        self.t(nums, expected)

    def test2(self):
        nums = [1,5,4,5]
        expected = 16
        self.t(nums, expected)

    def test3(self):
        nums = [3, 7]
        expected = 12
        self.t(nums, expected)

    def test4(self):
        nums = [7, 4]
        expected = 18
        self.t(nums, expected)

    def test5(self):
        nums = [1,8,1,5,10,10,10,7,3,3,9,4,1]
        expected = 81
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()