import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s, target, expected=None):
        result = Solution().rearrangeCharacters(s, target)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = 'abcba'
        target = 'abc'
        expected = 1
        self.t(s, target, expected)

    def test2(self):
        s = "abbaccaddaeea"
        target = "aaaaa"
        expected = 1
        self.t(s, target, expected)

    def test3(self):
        s = "aaaaaaaa"
        target = "a"
        expected = 8
        self.t(s, target, expected)


if __name__ == '__main__':
    unittest.main()