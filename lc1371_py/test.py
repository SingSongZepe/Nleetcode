import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().findTheLongestSubstring(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = 'eleetminicoworoep'
        expected = 13
        self.t(s, expected)

    def test2(self):
        s = 'leetcodeisgreat'
        expected = 5
        self.t(s, expected)

    def test3(self):
        s = 'bcbcbc'
        expected = 6
        self.t(s, expected)

if __name__ == '__main__':
    unittest.main()