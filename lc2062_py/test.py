import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().countVowelSubstrings(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        word = 'aeiouu'
        expected = 2
        self.t(word, expected)

    def test2(self):
        word = "unicornarihan"
        expected = 0
        self.t(word, expected)

    def test3(self):
        word = "cuaieuouac"
        expected = 7
        self.t(word, expected)


if __name__ == '__main__':
    unittest.main()