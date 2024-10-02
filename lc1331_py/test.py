import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().arrayRankTransform(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        arr = [40, 10, 20, 30]
        expected = [4, 1, 2, 3]
        self.t(arr, expected)

    def test2(self):
        arr = [100, 100, 100]
        expected = [1, 1, 1]
        self.t(arr, expected)

    def test3(self):
        arr = [37,12,28,9,100,56,80,5,12]
        expected = [5,3,4,2,8,6,7,1,3]
        self.t(arr, expected)


if __name__ == '__main__':
    unittest.main()