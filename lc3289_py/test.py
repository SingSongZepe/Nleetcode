import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().getSneakyNumbers(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [0, 1, 1, 0]
        expected = [0, 1]
        self.t(nums, expected)

    def test2(self):
        nums = [0,3,2,1,3,2]
        expected = [2, 3]
        self.t(nums, expected)

    def test3(self):
        nums = [7,1,5,4,3,4,6,0,9,5,8,2]
        expected = [4, 5]
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()