import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minAddToMakeValid(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = '())'
        expected = 1
        self.t(s, expected)

    def test2(self):
        s = '((('
        expected = 3
        self.t(s, expected)

    def test3(self):
        s = '(()()'
        expected = 1
        self.t(s, expected)

    def test4(self):
        s = '(((())('
        expected = 3
        self.t(s, expected)

    def test5(self):
        s = "()))(("
        expected = 4
        self.t(s, expected)

    def test6(self):
        s = "(()))))("
        expected = 4
        self.t(s, expected)

    def test7(self):
        s = ")())("
        expected = 3
        self.t(s, expected)


if __name__ == '__main__':
    unittest.main()