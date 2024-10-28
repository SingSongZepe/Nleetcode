import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().similarPairs(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        words = ['aba', 'aabb', 'abcd', 'bac', 'aabc']
        expected = 2
        self.t(words, expected)

    def test2(self):
        words = ["aabb", "ab", "ba"]
        expected = 3
        self.t(words, expected)


if __name__ == '__main__':
    unittest.main()