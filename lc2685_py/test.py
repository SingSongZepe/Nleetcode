import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, n, edges, expected=None):
        result = Solution().countCompleteComponents(n, edges)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 6
        edges = [[0,1],[0,2],[1,2],[3,4]]
        expected = 3
        self.t(n, edges, expected)

    def test2(self):
        n = 6
        edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
        expected = 1
        self.t(n, edges, expected)


if __name__ == '__main__':
    unittest.main()