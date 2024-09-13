import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, allowed, words, expected=None):
        result = Solution().countConsistentStrings(allowed, words)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        allowed = 'ab'
        words = ["ad", "bd", "aaab", "baa", "badab"]
        expected = 2
        self.t(allowed, words, expected)

    def test2(self):
        allowed = 'abc'
        words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
        expected = 7
        self.t(allowed, words, expected)

    def test3(self):
        allowed = 'cad'
        words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
        expected = 4
        self.t(allowed, words, expected)

if __name__ == '__main__':
    unittest.main()