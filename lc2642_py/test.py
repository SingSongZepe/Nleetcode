import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):

        pass
        
    def test1(self):
        graph = Graph3(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
        # d = graph.shortestPath(3, 2)
        # print(d)
        # d = graph.shortestPath(0, 3)
        # print(d)
        graph.addEdge([1, 3, 4])
        d = graph.shortestPath(0, 3)
        print(d)

if __name__ == '__main__':
    unittest.main()