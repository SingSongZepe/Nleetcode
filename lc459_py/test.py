import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().repeatedSubstringPattern(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = 'abab'
        expected = True
        self.t(s, expected)

    def test2(self):
        s = 'aba'
        expected = False
        self.t(s, expected)

    def test3(self):
        s = 'abcabcabcabc'
        expected = True
        self.t(s, expected)

    def test4(self):
        s = 'abac'
        expected = False
        self.t(s, expected)

    def test5(self):
        s = 'abcabc'
        expected = True
        self.t(s, expected)

    def test6(self):
        s = "abaababaab"
        expected = True
        self.t(s, expected)

if __name__ == '__main__':
    unittest.main()