import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, sentence1, sentence2, expected=None):
        result = Solution().areSentencesSimilar(sentence1, sentence2)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        sentence1 = "My name is Haley"
        sentence2 = "My Haley"
        expected = True
        self.t(sentence1, sentence2, expected)

    def test2(self):
        sentence1 = "of"
        sentence2 = "A lot of words"
        expected = False
        self.t(sentence1, sentence2, expected)

    def test3(self):
        sentence1 = "Eating right now"
        sentence2 = "Eating"
        expected = True
        self.t(sentence1, sentence2, expected)

    def test4(self):
        sentence1 = "Eating right now"
        sentence2 = "now"
        expected = True
        self.t(sentence1, sentence2, expected)

    def test5(self):
        sentence1 = "c h p Ny"
        sentence2 = "c BDQ r h p Ny"
        expected = True
        self.t(sentence1, sentence2, expected)

    def test6(self):
        sentence1 = "qbaVXO Msgr aEWD v ekcb"
        sentence2 = "Msgr aEWD ekcb"
        expected = False
        self.t(sentence1, sentence2, expected)

    def test7(self):
        sentence1 = "eTUny i b R UFKQJ EZx JBJ Q xXz"
        sentence2 = "eTUny i R EZx JBJ xXz"
        expected = False
        self.t(sentence1, sentence2, expected)


if __name__ == '__main__':
    unittest.main()