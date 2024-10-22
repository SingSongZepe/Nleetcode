import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, n, start, expected=None):
        result = Solution().xorOperation(n, start)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 5
        start = 0
        expected = 8
        self.t(n, start, expected)

    def test2(self):
        n = 4
        start = 3
        expected = 8
        self.t(n, start, expected)

if __name__ == '__main__':
    unittest.main()