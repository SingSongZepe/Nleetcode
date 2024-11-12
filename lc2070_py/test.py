import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, items, queries, expected=None):
        result = Solution().maximumBeauty(items, queries)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        items = [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]]
        queries = [1, 2, 3, 4, 5, 6]
        expected = [2, 4, 5, 5, 6, 6]
        self.t(items, queries, expected)

    def test2(self):
        items = [[1,2],[1,2],[1,3],[1,4]]
        queries = [1]
        expected = [4]
        self.t(items, queries, expected)

    def test3(self):
        items = [[10,1000]]
        queries = [5]
        expected = [0]
        self.t(items, queries, expected)




if __name__ == '__main__':
    unittest.main()