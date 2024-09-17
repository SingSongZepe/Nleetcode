import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minimumAbsDifference(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        arr = [4, 2, 1, 3]
        expected = [[1, 2], [2, 3], [3, 4]]
        self.t(arr, expected)

    def test2(self):
        arr = [1, 3, 6, 10, 15]
        expected = [[1, 3]]
        self.t(arr, expected)

    def test3(self):
        arr = [3, 8, -10, 23, 19, -4, -14, 27]
        expected = [[-14, -10], [19, 23], [23, 27]]
        self.t(arr, expected)

if __name__ == '__main__':
    unittest.main()