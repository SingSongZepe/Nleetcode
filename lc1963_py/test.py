import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minSwaps(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().minSwaps(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = '][]['
        expected = 1
        self.t(s, expected)

    def test2(self):
        s = '[]'
        expected = 0
        self.t(s, expected)

    def test3(self):
        s = "]]][[["
        expected = 2
        self.t(s, expected)

    def test11(self):
        s = '][]['
        expected = 1
        self.t1(s, expected)

    def test21(self):
        s = '[]'
        expected = 0
        self.t1(s, expected)

    def test31(self):
        s = "]]][[["
        expected = 2
        self.t1(s, expected)

if __name__ == '__main__':
    unittest.main()