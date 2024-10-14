import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, k, expected=None):
        result = Solution().maxKelements(nums, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [10, 10, 10, 10, 10]
        k = 5
        expected = 50
        self.t(nums, k, expected)

    def test2(self):
        nums = [1, 10, 3, 3, 3]
        k = 3
        expected = 17
        self.t(nums, k, expected)



if __name__ == '__main__':
    unittest.main()