import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().trailingZeroes(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 3
        expected = 0
        self.t(n, expected)

    def test2(self):
        n = 5
        expected = 1
        self.t(n, expected)

    def test3(self):
        n = 0
        expected = 0
        self.t(n, expected)


    def test4(self):
        n = 25
        expected = 6
        self.t(n, expected)

    def test5(self):
        n = 50
        expected = 12
        self.t(n, expected)

if __name__ == '__main__':
    unittest.main()