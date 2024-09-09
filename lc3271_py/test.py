import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s, k, expected=None):
        result = Solution().stringHash(s, k)
        print(result)
        self.assertEqual(result, expected)

        
    def test1(self):
        s = 'abcd'
        k = 2
        expected = 'bf'
        self.t(s, k, expected)

    def test2(self):
        s = 'mxz'
        k = 3
        expected = 'i'
        self.t(s, k, expected)


    def test_get_value(self):
        s = 'abcd'
        print(get_value(s))

if __name__ == '__main__':
    unittest.main()