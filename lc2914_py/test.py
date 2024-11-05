import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minChanges(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = '1001'
        expected = 2
        self.t(s, expected)

    def test2(self):
        s = '10'
        expected = 1
        self.t(s, expected)

    def test3(self):
        s = '10010100000111001101011000000010110011'
        expected = 8
        self.t(s, expected)


if __name__ == '__main__':
    unittest.main()