import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().isValid(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        word = 'b3'
        expected = False
        self.t(word, expected)

    def test2(self):
        word = 'a3$e'
        expected = False
        self.t(word, expected)

    def test3(self):
        word = "Ya$"
        expected = False
        self.t(word, expected)

if __name__ == '__main__':
    unittest.main()