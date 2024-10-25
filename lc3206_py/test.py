import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().numberOfAlternatingGroups(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        colors = [1, 1, 1]
        expected = 0
        self.t(colors, expected)

    def test2(self):
        colors = [0, 1, 0, 0, 1]
        expected = 3
        self.t(colors, expected)

    def test4(self):
        colors = [0, 1, 0, 0, 1, 0, 0]
        expected = 2
        self.t(colors, expected)

if __name__ == '__main__':
    unittest.main()