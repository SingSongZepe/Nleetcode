import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, sentence, searchWord, expected=None):
        result = Solution().isPrefixOfWord(sentence, searchWord)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, sentence, searchWord, expected=None):
        result = Solution1().isPrefixOfWord(sentence, searchWord)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        sentence = 'i love eating burger'
        searchWord = 'burg'
        expected = 4
        self.t(sentence, searchWord, expected)

    def test2(self):
        sentence = 'this problem is an easy problem'
        searchWord = 'pro'
        expected = 2
        self.t(sentence, searchWord, expected)

    def test3(self):
        sentence = 'i am tired'
        searchWord = 'you'
        expected = -1
        self.t(sentence, searchWord, expected)

    def test4(self):
        sentence = "hellohello hellohellohello"
        searchWord = "ell"
        expected = -1
        self.t(sentence, searchWord, expected)


    def test11(self):
        sentence = 'i love eating burger'
        searchWord = 'burg'
        expected = 4
        self.t1(sentence, searchWord, expected)

    def test21(self):
        sentence = 'this problem is an easy problem'
        searchWord = 'pro'
        expected = 2
        self.t1(sentence, searchWord, expected)

    def test31(self):
        sentence = 'i am tired'
        searchWord = 'you'
        expected = -1
        self.t1(sentence, searchWord, expected)

    def test41(self):
        sentence = "hellohello hellohellohello"
        searchWord = "ell"
        expected = -1
        self.t1(sentence, searchWord, expected)

if __name__ == '__main__':
    unittest.main()