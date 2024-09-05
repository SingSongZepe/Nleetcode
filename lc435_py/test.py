import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().eraseOverlapIntervals(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        intervals = [[1,2],[2,3],[3,4],[1,3]]
        expected = 1
        self.t(intervals, expected)

    def test2(self):
        intervals = [[1,2],[1,2],[1,2]]
        expected = 2
        self.t(intervals, expected)

    def test3(self):
        intervals = [[1,2],[2,3]]
        expected = 0
        self.t(intervals, expected)

    def test4(self):
        intervals = [[1,100],[11,22],[1,11],[2,12]]
        expected = 2
        self.t(intervals, expected)

if __name__ == '__main__':
    unittest.main()