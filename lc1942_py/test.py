import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, times, targetFriend, expected=None):
        result = Solution().smallestChair(times, targetFriend)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        times = [[1, 4], [2, 3], [4, 6]]
        targetFriend = 1
        expected = 1
        self.t(times, targetFriend, expected)

    def test2(self):
        times = [[3, 10], [1, 5], [2, 6]]
        targetFriend = 0
        expected = 2
        self.t(times, targetFriend, expected)

    def test3(self):
        times = [[33889, 98676], [80071, 89737], [44118, 52565], [52992, 84310], [78492, 88209], [21695, 67063], [84622, 95452],
         [98048, 98856], [98411, 99433], [55333, 56548], [65375, 88566], [55011, 62821], [48548, 48656], [87396, 94825],
         [55273, 81868], [75629, 91467]]
        targetFriend = 6
        expected = 2
        self.t(times, targetFriend, expected)


if __name__ == '__main__':
    unittest.main()