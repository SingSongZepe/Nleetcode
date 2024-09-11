import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().triangleNumber(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [2, 2, 3, 4]
        expected = 3
        self.t(nums, expected)

    def test2(self):
        nums = [4, 2, 3, 4]
        expected = 4
        self.t(nums, expected)

if __name__ == '__main__':
    unittest.main()