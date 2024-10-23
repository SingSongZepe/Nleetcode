import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, n, edges, source, destination, expected=None):
        result = Solution().validPath(n, edges, source, destination)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 3
        edges = [[0, 1], [1, 2], [2, 0]]
        source = 0
        destination = 2
        expected = True
        self.t(n, edges, source, destination, expected)


    def test2(self):
        n = 10
        edges = [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
        source = 7
        destination = 5
        expected = True
        self.t(n, edges, source, destination, expected)



if __name__ == '__main__':
    unittest.main()