import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, fronts, backs, expected=None):
        result = Solution().flipgame(fronts, backs)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, fronts, backs, expected=None):
        result = Solution1().flipgame(fronts, backs)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        fronts = [1, 2, 4, 4, 7]
        backs = [1, 3, 4, 1, 3]
        expected = 2
        self.t(fronts, backs, expected)

    def test2(self):
        fronts = [1]
        backs = [1]
        expected = 0
        self.t(fronts, backs, expected)

    def test3(self):
        fronts = [1, 1]
        backs = [1, 1]
        expected = 0
        self.t(fronts, backs, expected)

    def test11(self):
        fronts = [1, 2, 4, 4, 7]
        backs = [1, 3, 4, 1, 3]
        expected = 2
        self.t1(fronts, backs, expected)

    def test21(self):
        fronts = [1]
        backs = [1]
        expected = 0
        self.t1(fronts, backs, expected)

    def test31(self):
        fronts = [1, 1]
        backs = [1, 1]
        expected = 0
        self.t1(fronts, backs, expected)

if __name__ == '__main__':
    unittest.main()