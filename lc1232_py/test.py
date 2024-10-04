import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().checkStraightLine(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
        expected = True
        self.t(coordinates, expected)

    def test2(self):
        coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
        expected = False
        self.t(coordinates, expected)

    def test3(self):
        coordinates = [[1,1],[1,2], [2,2]]
        expected = False
        self.t(coordinates, expected)

    def test4(self):
        coordinates = [[1,1],[2,1], [2,2]]
        expected = False
        self.t(coordinates, expected)


if __name__ == '__main__':
    unittest.main()