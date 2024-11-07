import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().largestCombination(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        candidates = [16, 17, 71, 62, 12, 24, 14]
        expected = 4
        self.t(candidates, expected)

    def test2(self):
        candidates = [8, 8]
        expected = 2
        self.t(candidates, expected)

    def test3(self):
        candidates = [16,16,48,71,62,12,24,14,17,18,19,20,10000]
        expected = 10
        self.t(candidates, expected)


if __name__ == '__main__':
    unittest.main()