import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().isBoomerang(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        points = [[1,1],[2,3],[3,2]]
        expected = True
        self.t(points, expected)

    def test2(self):
        points = [[1,1],[2,2],[3,3]]
        expected = False
        self.t(points, expected)

if __name__ == '__main__':
    unittest.main()