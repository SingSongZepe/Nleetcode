import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maxPower(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().maxPower(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = 'leetcode'
        expected = 2
        self.t(s, expected)

    def test2(self):
        s = 'abbcccddddeeeeedcba'
        expected = 5
        self.t(s, expected)

    def test11(self):
        s = 'leetcode'
        expected = 2
        self.t1(s, expected)

    def test21(self):
        s = 'abbcccddddeeeeedcba'
        expected = 5
        self.t1(s, expected)

if __name__ == '__main__':
    unittest.main()