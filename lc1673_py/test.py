import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums, k, expected=None):
        result = Solution().mostCompetitive(nums, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums = [3, 5, 2, 6]
        k = 2
        expected = [2, 6]
        self.t(nums, k, expected)

    def test2(self):
        nums = [2,4,3,3,5,4,9,6]
        k = 4
        expected = [2, 3, 3, 4]
        self.t(nums, k, expected)


if __name__ == '__main__':
    unittest.main()