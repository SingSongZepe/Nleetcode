import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().numTimesAllBlue(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().numTimesAllBlue(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        flips = [3, 2, 4, 1, 5]
        expected = 2
        self.t(flips, expected)

    def test2(self):
        flips = [4, 1, 2, 3]
        expected = 1
        self.t(flips, expected)

    def test11(self):
        flips = [3, 2, 4, 1, 5]
        expected = 2
        self.t1(flips, expected)

    def test21(self):
        flips = [4, 1, 2, 3]
        expected = 1
        self.t1(flips, expected)

if __name__ == '__main__':
    unittest.main()