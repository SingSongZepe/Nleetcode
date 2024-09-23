import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().oddString(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        words = ['adc', 'wzy', 'abc']
        expected = 'abc'
        self.t(words, expected)

    def test2(self):
        words = ['aaa', 'bob', 'ccc', 'ddd']
        expected = 'bob'
        self.t(words, expected)

if __name__ == '__main__':
    unittest.main()