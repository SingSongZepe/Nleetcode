import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().countHillValley(arg)
        # self.assertEqual(result, expected)
        print(result)
        
    def test1(self):
        nums = [2, 4, 1, 1, 6, 5]
        self.t(nums)

    def test2(self):
        nums = [6, 6, 5, 5, 4, 1]
        self.t(nums)

    def test3(self):
        nums = [5,7,7,1,7]
        self.t(nums)

    def test4(self):
        nums = [85,52,89,81,48,8,18,12,88,20,70,100,67,42,12,95,57,8,41,82,37,44,47,18,46]
        expected = 15
        self.t(nums, expected)

    def test5(self):
        nums = [57,57,57,57,57,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,85,85,85,86,86,86]
        expected = 2
        self.t(nums, expected)


    # def test_loop(self):
    #
    #     for i in range(100):
    #         print(i)

if __name__ == '__main__':
    unittest.main()