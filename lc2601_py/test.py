
from main import *

from twisted.trial import unittest

class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().primeSubOperation(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [4, 9, 6, 10]
        expected = True
        self.t(nums, expected)

    def test2(self):
        nums = [6,8,11,12]
        expected = True
        self.t(nums, expected)

    def test3(self):
        nums = [5, 8, 3]
        expected = False
        self.t(nums, expected)

    def test4(self):
        nums = [2, 2]
        expected = False
        self.t(nums, expected)

    def test5(self):
        nums = [998, 2]
        expected = True
        self.t(nums, expected)



    def test_bisect(self):
        num = 7
        print(find_left_prime(num))
        print(find_left_prime(2))

    def test_bisect1(self):
        num = 4
        if v := find_left_prime(num):
            print(v)
