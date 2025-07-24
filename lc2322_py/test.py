import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minimumScore(*arg)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        nums = [1, 5, 5, 4, 11]
        edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
        expected = 9
        self.t([nums, edges], expected)

    def test2(self):
        nums = [5, 5, 2, 4, 4, 2]
        edges = [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]
        expected = 0
        self.t([nums, edges], expected)

    def test3(self):
        nums = [29,29,23,32,17]
        edges = [[3,1],[2,3],[4,1],[0,4]]
        expected = 15
        self.t([nums, edges], expected)

    def test4(self):
        nums = [26,20,10,20]
        edges = [[1,3],[1,2],[0,1]]
        expected = 10
        self.t([nums, edges], expected)


if __name__ == '__main__':
    unittest.main()