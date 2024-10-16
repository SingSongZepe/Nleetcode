import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s, indices, expected=None):
        result = Solution().restoreString(s, indices)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = 'codeleet'
        indices = [4, 5, 6, 7, 0, 2, 1, 3]
        expected = 'leetcode'
        self.t(s, indices, expected)

    def test2(self):
        s = 'abc'
        indices = [0, 1, 2]
        expected = 'abc'
        self.t(s, indices, expected)

if __name__ == '__main__':
    unittest.main()