import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minimumPushes(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        word = "abcde"
        expected = 5
        self.t(word, expected)

    def test2(self):
        word = "xycdefghij"
        expected = 12
        self.t(word, expected)

if __name__ == '__main__':
    unittest.main()