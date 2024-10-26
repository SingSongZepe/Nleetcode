import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s, p, expected=None):
        result = Solution().findAnagrams(s, p)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = "cbaebabacd"
        p = "abc"
        expected = [0, 6]
        self.t(s, p, expected)

    def test2(self):
        s = "abab"
        p = "ab"
        expected = [0, 1, 2]
        self.t(s, p, expected)


if __name__ == '__main__':
    unittest.main()