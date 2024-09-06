import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minCostToMoveChips(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().minCostToMoveChips(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        position = [1, 2, 3]
        expected = 1
        self.t(position, expected)

    def test2(self):
        position = [2, 2, 2, 3, 3]
        expected = 2
        self.t(position, expected)

    def test3(self):
        position = [1, 1000000000]
        expected = 1
        self.t(position, expected)

    def test11(self):
        position = [1, 2, 3]
        expected = 1
        self.t1(position, expected)

    def test21(self):
        position = [2, 2, 2, 3, 3]
        expected = 2
        self.t1(position, expected)

    def test31(self):
        position = [1, 1000000000]
        expected = 1
        self.t1(position, expected)


if __name__ == '__main__':
    unittest.main()