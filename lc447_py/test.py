import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution1().numberOfBoomerangs(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        points = [[0, 0], [1, 0], [2, 0]]
        expected = 2
        self.t(points, expected)

    def test2(self):
        points = [[1, 1], [2, 2], [3, 3]]
        expected = 2
        self.t(points, expected)

    def test3(self):
        points = [[1, 1]]
        expected = 0
        self.t(points, expected)

    def test4(self):
        points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
        expected = 20
        self.t(points, expected)



if __name__ == '__main__':
    unittest.main()