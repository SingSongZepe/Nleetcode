import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums1, nums2, expected=None):
        result = Solution().minNumber(nums1, nums2)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        nums1 = [4, 1, 3]
        nums2 = [5, 7]
        expected = 15
        self.t(nums1, nums2, expected)

    def test2(self):
        nums1 = [3, 5, 2, 6]
        nums2 = [3, 1, 7]
        expected = 3
        self.t(nums1, nums2, expected)

if __name__ == '__main__':
    unittest.main()