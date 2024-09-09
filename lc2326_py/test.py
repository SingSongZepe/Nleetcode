import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, m, n, head, expected=None):
        result = Solution().spiralMatrix(m, n, head)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, m, n, head, expected=None):
        result = Solution1().spiralMatrix(m, n, head)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        m = 3
        n = 5
        head = build_list([3,0,2,6,8,1,7,9,4,2,5,5,0])
        expected = [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]
        self.t(m, n, head, expected)

    def test2(self):
        m = 1
        n = 4
        head = build_list([0, 1, 2])
        expected = [[0, 1, 2, -1]]
        self.t(m, n, head, expected)

    def test11(self):
        m = 3
        n = 5
        head = build_list([3,0,2,6,8,1,7,9,4,2,5,5,0])
        expected = [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]
        self.t1(m, n, head, expected)

    def test21(self):
        m = 1
        n = 4
        head = build_list([0, 1, 2])
        expected = [[0, 1, 2, -1]]
        self.t1(m, n, head, expected)


if __name__ == '__main__':
    unittest.main()