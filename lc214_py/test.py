import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().shortestPalindrome(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = 'aacecaaa'
        expected = 'aaacecaaa'
        self.t(s, expected)

    def test2(self):
        s = 'abcd'
        expected = 'dcbabcd'
        self.t(s, expected)

if __name__ == '__main__':
    unittest.main()