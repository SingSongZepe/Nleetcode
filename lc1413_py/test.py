import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minStartValue(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [-3, 2, -3, 4, 2]
        expected = 5
        self.t(nums, expected)

    def test2(self):
        nums = [1, 2]
        expected = 1
        self.t(nums, expected)

    def test3(self):
        nums = [1, -2, -3]
        expected = 5
        self.t(nums, expected)



if __name__ == '__main__':
    unittest.main()