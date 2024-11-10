import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().sumOfTheDigitsOfHarshadNumber(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        x = 18
        expected = 9
        self.t(x, expected)

    def test2(self):
        x = 23
        expected = -1
        self.t(x, expected)

if __name__ == '__main__':
    unittest.main()