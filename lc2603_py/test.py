import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, coins, edges, expected=None):
        result = Solution().collectTheCoins(coins, edges)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        coins = [1, 0, 0, 0, 0, 1]
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
        expected = 2
        self.t(coins, edges, expected)

    def test2(self):
        coins = [0,0,0,1,1,0,0,1]
        edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
        expected = 2
        self.t(coins, edges, expected)



if __name__ == '__main__':
    unittest.main()