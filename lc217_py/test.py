import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().containsDuplicate(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [1, 2, 3, 1]
        expected = True
        self.t(nums, expected)

    def test2(self):
        nums = [1, 2, 3, 4]
        expected = False
        self.t(nums, expected)

    def test3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        expected = True
        self.t(nums, expected)



if __name__ == '__main__':
    unittest.main()