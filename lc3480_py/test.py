import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maxSubarrays(*arg)
        print(result)
        
    def test1(self):
        n = 5
        conflictingPairs = [[1, 2], [2, 5], [3, 5]]
        expected = 12
        self.t([n, conflictingPairs], expected)

    def test2(self):
        n = 4
        conflictingPairs = [[2, 3], [1, 4]]
        expected = 9
        self.t([n, conflictingPairs], expected)


if __name__ == '__main__':
    unittest.main()