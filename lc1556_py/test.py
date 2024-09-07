import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().thousandSeparator(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 987
        expected = "987"
        self.t(n, expected)

    def test2(self):
        n = 1234
        expected = "1.234"
        self.t(n, expected)

    def test3(self):
        n = 123456
        expected = "123.456"
        self.t(n, expected)

    def test4(self):
        n = 1234567
        expected = "1.234.567"
        self.t(n, expected)

    def test5(self):
        n = 0
        expected = "0"
        self.t(n, expected)

if __name__ == '__main__':
    unittest.main()