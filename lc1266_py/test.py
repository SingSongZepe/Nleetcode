import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minTimeToVisitAllPoints(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        points = [[1, 1], [3, 4], [-1, 0]]
        expected = 7
        self.t(points, expected)

    def test2(self):
        points = [[3, 2], [-2, 2]]
        expected = 5
        self.t(points, expected)

if __name__ == '__main__':
    unittest.main()