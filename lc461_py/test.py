import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, x, y, expected=None):
        result = Solution().hammingDistance(x, y)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        x = 1
        y = 4
        expected = 2
        self.t(x, y, expected)

    def test2(self):
        x = 3
        y = 1
        expected = 1
        self.t(x, y, expected)

if __name__ == '__main__':
    unittest.main()