import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maxRotateFunction(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [4, 3, 2, 6]
        expected = 26
        self.t(nums, expected)

    def test2(self):
        nums = [100]
        expected = 0
        self.t(nums, expected)


if __name__ == '__main__':
    unittest.main()