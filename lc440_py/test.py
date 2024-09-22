import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, n, k, expected=None):
        result = Solution().findKthNumber(n, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 13
        k = 2
        expected = 10
        self.t(n, k, expected)

    def test2(self):
        n = 1
        k = 1
        expected = 1
        self.t(n, k, expected)

if __name__ == '__main__':
    unittest.main()