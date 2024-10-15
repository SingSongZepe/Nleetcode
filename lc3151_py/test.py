import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().isArraySpecial(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1]
        expected = True
        self.t(nums, expected)

    def test2(self):
        nums = [2, 1, 4]
        expected = True
        self.t(nums, expected)

    def test3(self):
        nums = [4, 3, 1, 6]
        expected = False
        self.t(nums, expected)


if __name__ == '__main__':
    unittest.main()