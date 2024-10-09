import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().reformat(arg)
        print(result)
        # self.assertEqual(result, expected)
        
    def test1(self):
        s = 'a0b1c2'
        expected = '0a1b2c'
        self.t(s, expected)

    def test2(self):
        s = 'leetcode'
        expected = 'leetcode'
        self.t(s, expected)

    def test3(self):
        s = '1229857369'
        expected = ''
        self.t(s, expected)

    def test4(self):
        s = 'a0b1c29'
        expected = '0a1b2c'
        self.t(s, expected)


if __name__ == '__main__':
    unittest.main()