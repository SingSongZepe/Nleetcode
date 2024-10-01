import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s, p, expected=None):
        result = Solution().isMatch(s, p)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = 'aa'
        p = 'a'
        expected = False
        self.t(s, p, expected)

    def test2(self):
        s = 'aa'
        p = '*'
        expected = True
        self.t(s, p, expected)

    def test3(self):
        s = 'cb'
        p = '?a'
        expected = False
        self.t(s, p, expected)

if __name__ == '__main__':
    unittest.main()