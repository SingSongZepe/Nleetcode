import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, aliceSizes, bobSizes, expected=None):
        result = Solution().fairCandySwap(aliceSizes, bobSizes)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        aliceSizes = [1, 1]
        bobSizes = [2, 2]
        expected = [1, 2]
        self.t(aliceSizes, bobSizes, expected)

    def test2(self):
        aliceSizes = [1, 2]
        bobSizes = [2, 3]
        expected = [1, 2]
        self.t(aliceSizes, bobSizes, expected)

    def test3(self):
        aliceSizes = [2]
        bobSizes = [1, 3]
        expected = [2, 3]
        self.t(aliceSizes, bobSizes, expected)

if __name__ == '__main__':
    unittest.main()