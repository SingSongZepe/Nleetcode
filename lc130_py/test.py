import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        Solution().solve(arg)
        print(arg)
        self.assertEqual(arg, expected)

        
    def test1(self):
        board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
        expected = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

        self.t(board, expected)

    def test2(self):
        board = [["X"]]
        expected = [["X"]]

        self.t(board, expected)

if __name__ == '__main__':
    unittest.main()