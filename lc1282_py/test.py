import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().groupThePeople(arg)
        print(result)

        
    def test1(self):
        groupSizes = [3, 3, 3, 3, 3, 1, 3]
        expected = [[5], [0, 1, 2], [3, 4, 6]]
        self.t(groupSizes, expected)

    def test2(self):
        groupSizes = [2, 1, 3, 3, 3, 2]
        expected = [[1], [0, 5], [2, 3, 4]]
        self.t(groupSizes, expected)

if __name__ == '__main__':
    unittest.main()