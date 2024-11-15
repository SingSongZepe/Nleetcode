import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().numSpecial(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
        expected = 1
        self.t(mat, expected)

    def test2(self):
        mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        expected = 3
        self.t(mat, expected)

if __name__ == '__main__':
    unittest.main()