import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().compress(arg)
        print(result)
        print(arg[:result])
        self.assertEqual(result, expected)
        
    def test1(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        expected = 6
        self.t(chars, expected)

    def test2(self):
        chars = ["a"]
        expected = 1
        self.t(chars, expected)

    def test3(self):
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        expected = 4
        self.t(chars, expected)

    def test4(self):
        chars = ["a","a","a","b","b","a","a"]
        expected = 6
        self.t(chars, expected)


if __name__ == '__main__':
    unittest.main()