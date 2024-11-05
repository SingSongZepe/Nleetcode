import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, nums1, nums2, k, expected=None):
        result = Solution().numberOfPairs(nums1, nums2, k)
        print(result)
        
    def test1(self):
        nums1 = [1,3,4]
        nums2 = [3,4,1]
        k = 1
        expected = 5
        self.t(nums1, nums2, k, expected)

    def test2(self):
        nums1 = [1,2,4,12]
        nums2 = [2,4]
        k = 3
        expected = 2
        self.t(nums1, nums2, k, expected)

if __name__ == '__main__':
    unittest.main()