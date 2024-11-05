import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().compressedString(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        word = 'abcde'
        expected = "1a1b1c1d1e"
        self.t(word, expected)

    def test2(self):
        word = "aaaaaaaaaaaaaabb"
        expected = "9a5a2b"
        self.t(word, expected)


if __name__ == '__main__':
    unittest.main()