import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minTimeToType(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        word = 'abc'
        expected = 5
        self.t(word, expected)

    def test2(self):
        word = 'bza'
        expected = 7
        self.t(word, expected)

if __name__ == '__main__':
    unittest.main()