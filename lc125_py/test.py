import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().isPalindrome(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = "A man, a plan, a canal: Panama"
        expected = True
        self.t(s, expected)

    def test2(self):
        s = "race a car"
        expected = False
        self.t(s, expected)

    def test3(self):
        s = " "
        expected = True
        self.t(s, expected)

    def test5(self):
        s = "0P"
        expected = False
        self.t(s, expected)

if __name__ == '__main__':
    unittest.main()