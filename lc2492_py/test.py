import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, n, roads, expected=None):
        result = Solution().minScore(n, roads)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 4
        roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
        expected = 5
        self.t(n, roads, expected)

    def test2(self):
        n = 4
        roads = [[1,2,2],[1,3,4],[3,4,7]]
        expected = 2
        self.t(n, roads, expected)


if __name__ == '__main__':
    unittest.main()