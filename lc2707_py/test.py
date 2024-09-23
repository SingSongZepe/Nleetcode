import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s, dictionary, expected=None):
        result = Solution().minExtraChar(s, dictionary)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, s, dictionary, expected=None):
        result = Solution1().minExtraChar(s, dictionary)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        s = 'leetscode'
        dictionary = ['leet', 'code', 'leetcode']
        expected = 1
        self.t(s, dictionary, expected)

    def test2(self):
        s = 'sayhelloworld'
        dictionary = ['hello', 'world']
        expected = 3
        self.t(s, dictionary, expected)

    def test11(self):
        s = 'leetscode'
        dictionary = ['leet', 'code', 'leetcode']
        expected = 1
        self.t1(s, dictionary, expected)

    def test21(self):
        s = 'sayhelloworld'
        dictionary = ['hello', 'world']
        expected = 3
        self.t1(s, dictionary, expected)


if __name__ == '__main__':
    unittest.main()