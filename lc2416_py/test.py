import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().sumPrefixScores(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().sumPrefixScores(arg)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        words = ['abc', 'ab', 'bc', 'b']
        expected = [5, 4, 3, 2]
        self.t(words, expected)

    def test2(self):
        words = ['abcd']
        expected = [4]
        self.t(words, expected)

    def test11(self):
        words = ['abc', 'ab', 'bc', 'b']
        expected = [5, 4, 3, 2]
        self.t1(words, expected)

    def test21(self):
        words = ['abcd']
        expected = [4]
        self.t1(words, expected)

if __name__ == '__main__':
    unittest.main()