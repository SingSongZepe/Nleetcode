import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, queries, expected=None):
        result = Solution().xorQueries(arg, queries)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, queries, expected=None):
        result = Solution().xorQueries(arg, queries)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        arr = [1, 3, 4, 8]
        queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
        expected = [2, 7, 14, 8]
        self.t(arr, queries, expected)

    def test2(self):
        arr = [4, 8, 2, 10]
        queries = [[2, 3], [1, 3], [0, 0], [0, 3]]
        expected = [8, 0, 4, 4]
        self.t(arr, queries, expected)

    def test11(self):
        arr = [1, 3, 4, 8]
        queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
        expected = [2, 7, 14, 8]
        self.t1(arr, queries, expected)

    def test21(self):
        arr = [4, 8, 2, 10]
        queries = [[2, 3], [1, 3], [0, 0], [0, 3]]
        expected = [8, 0, 4, 4]
        self.t1(arr, queries, expected)

if __name__ == '__main__':
    unittest.main()