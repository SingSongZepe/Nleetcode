import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, a, b, c, expected=None):
        result = Solution().longestDiverseString(a, b, c)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        a = 1
        b = 1
        c = 7
        expected = "ccaccbcc"
        self.t(a, b, c, expected)

    def test2(self):
        a = 7
        b = 1
        c = 0
        expected = "aabaa"
        self.t(a, b, c, expected)

if __name__ == '__main__':
    unittest.main()