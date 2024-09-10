import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().modifyString(arg)
        print(result)
        # self.assertEqual(result, expected)

    def t2(self, arg, expected=None):
        result = Solution2().modifyString(arg)
        print(result)
        # self.assertEqual(result, expected)
        
    def test1(self):
        s = '?zs'
        expected = 'azs'
        self.t(s, expected)

    def test2(self):
        s = 'ubv?w'
        expected = 'ubvaw'
        self.t(s, expected)

    def test12(self):
        s = '?zs'
        expected = 'azs'
        self.t2(s, expected)

    def test22(self):
        s = 'ubv?w'
        expected = 'ubvaw'
        self.t2(s, expected)


if __name__ == '__main__':
    unittest.main()