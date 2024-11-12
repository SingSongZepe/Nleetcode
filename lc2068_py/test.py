import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, word1, word2, expected=None):
        result = Solution().checkAlmostEquivalent(word1, word2)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        word1 = "abcdeef"
        word2 = "abaaacc"
        expected = True
        self.t(word1, word2, expected)

    def test2(self):
        word1 = "cccddabba"
        word2 = "babababab"
        expected = True
        self.t(word1, word2, expected)

    def test3(self):
        word1 = "aaaa"
        word2 = "bccb"
        expected = False
        self.t(word1, word2, expected)

    def test4(self):
        word2 = "iiiiii"
        word1 = "zzzyyy"
        expected = False
        self.t(word1, word2, expected)

if __name__ == '__main__':
    unittest.main()