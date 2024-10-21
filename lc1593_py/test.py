import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maxUniqueSplit(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = 'ababccc'
        expected = 5
        self.t(s, expected)

    def test2(self):
        s = 'aba'
        expected = 2
        self.t(s, expected)

    def test3(self):
        s = 'aa'
        expected = 1
        self.t(s, expected)

if __name__ == '__main__':
    unittest.main()