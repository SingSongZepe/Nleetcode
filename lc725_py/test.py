import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, head, k, expected=None):
        result = Solution().splitListToParts(head, k)
        for list in result:
            print_list(list)
        
    def test1(self):
        head = build_list([1, 2, 3])
        k = 5
        expected = [[1], [2], [3], [], []]
        self.t(head, k, expected)

    def test2(self):
        head = build_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        k = 3
        expected = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
        self.t(head, k, expected)

if __name__ == '__main__':
    unittest.main()