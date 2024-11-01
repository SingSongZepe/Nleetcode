import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().makeFancyString(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = 'leeetcode'
        expected = 'leetcode'
        self.t(s, expected)

    def test2(self):
        s = 'aaabaaaa'
        expected = 'aabaa'
        self.t(s, expected)

    def test3(self):
        s = 'aab'
        expected = 'aab'
        self.t(s, expected)

if __name__ == '__main__':
    unittest.main()