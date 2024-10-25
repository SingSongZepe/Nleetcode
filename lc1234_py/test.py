import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution1().balancedString(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = 'QWER'
        expected = 0
        self.t(s, expected)

    def test2(self):
        s = 'QQER'
        expected = 1
        self.t(s, expected)

    def test3(self):
        s = 'QQQW'
        expected = 2
        self.t(s, expected)

    def test4(self):
        s = 'WWEQERQWQWWRWWERQWEQ'
        expected = 4
        self.t(s, expected)

    def test5(self):
        s = "WQWRQQQW"
        expected = 3
        self.t(s, expected)

if __name__ == '__main__':
    unittest.main()