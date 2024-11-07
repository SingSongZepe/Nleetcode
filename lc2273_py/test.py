import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().removeAnagrams(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        words = ["abba","baba","bbaa","cd","cd"]
        expected = ['abba', 'cd']
        self.t(words, expected)

    def test2(self):
        words = ["a", "b", "c", "d", "e"]
        expected = ["a", "b", "c", "d", "e"]
        self.t(words, expected)

    def test3(self):
        words = ["z","z","z","gsw","wsg","gsw","krptu"]
        expected = ["z","gsw","krptu"]
        self.t(words, expected)

    def test4(self):
        words = ["a","b","a"]
        expected = ["a","b","a"]
        self.t(words, expected)

    def test5(self):
        words = ["az", "azz"]
        expected = ["az", "azz"]
        self.t(words, expected)


if __name__ == '__main__':
    unittest.main()