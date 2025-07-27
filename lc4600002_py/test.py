import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().numOfSubsequences(arg)
        self.assertEqual(result, expected)
        print(result)
        
    def test1(self):
        s = 'LMCT'
        expected = 2
        self.t(s, expected)

    def test2(self):
        s = 'CT'
        expected = 1
        self.t(s, expected)

    def test3(self):
        s = 'LCCT'
        expected = 4
        self.t(s, expected)


if __name__ == '__main__':
    unittest.main()