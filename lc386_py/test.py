import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().lexicalOrder(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 13
        expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        self.t(n, expected)

    def test2(self):
        n = 2
        expected = [1, 2]
        self.t(n, expected)

if __name__ == '__main__':
    unittest.main()