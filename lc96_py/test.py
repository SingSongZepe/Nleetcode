import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().numTrees(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 3
        expected = 5
        self.t(n, expected)

    def test2(self):
        n = 1
        expected = 1
        self.t(n, expected)

if __name__ == '__main__':
    unittest.main()