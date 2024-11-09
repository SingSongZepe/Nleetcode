import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, n, x, expected=None):
        result = Solution().minEnd(n, x)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 3
        x = 4
        expected = 6
        self.t(n, x, expected)

    def test2(self):
        n = 2
        x = 7
        expected = 15
        self.t(n, x, expected)

if __name__ == '__main__':
    unittest.main()