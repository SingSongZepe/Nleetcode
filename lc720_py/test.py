import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().longestWord(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().longestWord(arg)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        words = ["w","wo","wor","worl","world"]
        expected = "world"
        self.t(words, expected)

    def test2(self):
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        expected = "apple"
        self.t(words, expected)

    def test11(self):
        words = ["w","wo","wor","worl","world"]
        expected = "world"
        self.t1(words, expected)

    def test21(self):
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        expected = "apple"
        self.t1(words, expected)

if __name__ == '__main__':
    unittest.main()