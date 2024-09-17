import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, secret, guess, expected=None):
        result = Solution().getHint(secret, guess)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        secret = "1807"
        guess = "7810"
        expected = "1A3B"
        self.t(secret, guess, expected)

    def test2(self):
        secret = "1123"
        guess = "0111"
        expected = "1A1B"
        self.t(secret, guess, expected)

if __name__ == '__main__':
    unittest.main()