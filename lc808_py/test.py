import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().soupServings(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 50
        expected = 0.625
        self.t(n, expected)

    def test2(self):
        n = 100
        expected = 0.71875
        self.t(n, expected)


if __name__ == '__main__':
    unittest.main()