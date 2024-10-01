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
        self.t(s, p, expected=False)

    def test2(self):
        s = 'aa'
        p = 'a*'
        self.t(s, p, expected=True)

    def test3(self):
        s = 'ab'
        p = '.*'
        self.t(s, p, expected=True)

if __name__ == '__main__':
    unittest.main()