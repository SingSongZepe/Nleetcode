import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, words, order, expected=None):
        result = Solution().isAlienSorted(words, order)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        words = ['hello', 'leetcode']
        order = "hlabcdefgijkmnopqrstuvwxyz"
        expected = True
        self.t(words, order, expected)

    def test2(self):
        words = ["word", "world", "row"]
        order = "worldabcefghijkmnpqstuvxyz"
        expected = False
        self.t(words, order, expected)

    def test3(self):
        words = ["apple","app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        expected = False
        self.t(words, order, expected)

    def test4(self):
        words = ["hello", "hello"]
        order = "abcdefghijklmnopqrstuvwxyz"
        expected = True
        self.t(words, order, expected)


if __name__ == '__main__':
    unittest.main()