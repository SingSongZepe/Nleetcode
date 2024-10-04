import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, m, n, indices, expected=None):
        result = Solution().oddCells(m, n, indices)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        m = 2
        n = 3
        indices = [[0,1], [1,1]]
        expected = 6
        self.t(m, n, indices, expected)

    def test2(self):
        m = 2
        n = 2
        indices = [[1,1],[0,0]]
        expected = 0
        self.t(m, n, indices, expected)

if __name__ == '__main__':
    unittest.main()