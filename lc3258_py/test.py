import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s, k, expected=None):
        result = Solution().countKConstraintSubstrings(s, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = "10101"
        k = 1
        expected = 12
        self.t(s, k, expected)

    def test2(self):
        s = "1010101"
        k = 2
        expected =  25
        self.t(s, k, expected)


if __name__ == '__main__':
    unittest.main()