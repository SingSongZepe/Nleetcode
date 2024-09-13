import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s1, s2, s3, expected=None):
        result = Solution().isInterleave(s1, s2, s3)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        expected = True
        self.t(s1, s2, s3, expected)

    def test2(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        expected = False
        self.t(s1, s2, s3, expected)

    def test3(self):
        s1 = ""
        s2 = ""
        s3 = ""
        expected = True
        self.t(s1, s2, s3, expected)

if __name__ == '__main__':
    unittest.main()