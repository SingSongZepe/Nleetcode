import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().calculate(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = '1 + 1'
        expected = 2
        self.t(s, expected)

    def test2(self):
        s = ' 2-1 + 2 '
        expected = 3
        self.t(s, expected)

    def test3(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        expected = 23
        self.t(s, expected)


if __name__ == '__main__':
    unittest.main()