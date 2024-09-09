import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, start, d, expected=None):
        result = Solution().maxPossibleScore(start, d)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        start = [6, 0, 4]
        d = 2
        expected = 4
        self.t(start, d, expected)

    def test2(self):
        start = [2, 6, 13, 13]
        d = 5
        expected = 5
        self.t(start, d, expected)

    def test3(self):
        start = [1000000000,1000000000]
        d = 0
        expected = 0
        self.t(start, d, expected)

if __name__ == '__main__':
    unittest.main()