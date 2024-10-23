import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution1().findPrefixScore(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [2, 3, 7, 5, 10]
        expected = [4, 10, 24, 36, 56]
        self.t(nums, expected)

    def test2(self):
        nums = [1,1,2,4,8,16]
        expected = [2,4,8,16,32,64]
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()