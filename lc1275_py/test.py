import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().tictactoe(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
        expected = "A"
        self.t(moves, expected)

    def test2(self):
        moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
        expected = "B"
        self.t(moves, expected)

    def test3(self):
        moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
        expected = "Draw"
        self.t(moves, expected)


if __name__ == '__main__':
    unittest.main()