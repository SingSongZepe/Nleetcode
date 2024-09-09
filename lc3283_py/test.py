import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, kx, ky, positions, expected=None):
        result = Solution().maxMoves(kx, ky, positions)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        kx = 1
        ky = 1
        positions = [[0, 0]]
        expected = 4
        self.t(kx, ky, positions, expected)

    def test2(self):
        kx = 0
        ky = 2
        positions = [[1, 1], [2, 2], [3, 3]]
        expected = 8
        self.t(kx, ky, positions, expected)

    def test3(self):
        kx = 0
        ky = 0
        positions = [[1, 2], [2, 4]]
        expected = 3
        self.t(kx, ky, positions, expected)

if __name__ == '__main__':
    unittest.main()