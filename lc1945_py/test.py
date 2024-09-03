import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s, k, expected=None):
        result = Solution().getLucky(s, k)
        print(result)
        
    def test1(self):
        s = 'iiii'
        k = 1
        expected = 36
        self.t(s, expected)

    def test2(self):
        s = 'leetcode'
        k = 2
        expected = 6
        self.t(s, expected)

    def test3(self):
        s = 'zbax'
        k = 2
        expected = 8
        self.t(s, expected)

if __name__ == '__main__':
    unittest.main()