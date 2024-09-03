import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().findDisappearedNumbers(arg)
        print(result)

    def t1(self, arg, expected=None):
        result = Solution1().findDisappearedNumbers(arg)
        print(result)
        
    def test1(self):
        nums = [4,3,2,7,8,2,3,1]
        expected = [5,6]
        self.t(nums, expected)

    def test2(self):
        nums = [1,1]
        expected = [2]
        self.t(nums, expected)

    def test11(self):
        nums = [4,3,2,7,8,2,3,1]
        expected = [5,6]
        self.t1(nums, expected)

    def test21(self):
        nums = [1,1]
        expected = [2]
        self.t1(nums, expected)


if __name__ == '__main__':
    unittest.main()