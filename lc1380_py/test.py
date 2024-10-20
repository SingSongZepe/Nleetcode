import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().luckyNumbers(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        matrix = [[3,7,8],[9,11,13],[15,16,17]]
        expected = [15]
        self.t(matrix, expected)

    def test2(self):
        matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
        expected = [12]
        self.t(matrix, expected)

    def test3(self):
        matrix = [[7,8],[1,2]]
        expected = [7]
        self.t(matrix, expected)

if __name__ == '__main__':
    unittest.main()