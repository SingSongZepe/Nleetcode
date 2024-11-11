import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s, chars, vals, expected=None):
        result = Solution().maximumCostSubstring(s, chars, vals)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = "adaa"
        chars = "d"
        vals = [-1000]
        expected = 2
        self.t(s, chars, vals, expected)

    def test2(self):
        s = "abc"
        chars = "abc"
        vals = [-1,-1,-1]
        expected = 0
        self.t(s, chars, vals, expected)

    def test3(self):
        s = "kqqqqqkkkq"
        chars = "kq"
        vals = [-6,6]
        expected = 30
        self.t(s, chars, vals, expected)



if __name__ == '__main__':
    unittest.main()