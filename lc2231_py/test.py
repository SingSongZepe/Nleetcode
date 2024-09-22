import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().largestInteger(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        num = 1234
        expected = 3412
        self.t(num, expected)

    def test2(self):
        num = 65875
        expected = 87655
        self.t(num, expected)

    def test3(self):
        num = 456139
        expected = 694531
        self.t(num, expected)


if __name__ == '__main__':
    unittest.main()