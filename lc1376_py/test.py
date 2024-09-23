import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, n, headID, manager, informTime, expected=None):
        result = Solution().numOfMinutes(n, headID, manager, informTime)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, n, headID, manager, informTime, expected=None):
        result = Solution1().numOfMinutes(n, headID, manager, informTime)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 1
        headID = 0
        manager = [-1]
        informTime = [0]
        expected = 0
        self.t(n, headID, manager, informTime, expected)

    def test2(self):
        n = 6
        headID = 2
        manager = [2,2,-1,2,2,2]
        informTime = [0,0,1,0,0,0]
        expected = 1
        self.t(n, headID, manager, informTime, expected)

    # def test3(self):
    #     n = 22
    #     headID = 7,
    #     manager = [12, 7, 18, 11, 13, 21, 12, -1, 6, 5, 14, 13, 14, 9, 20, 13, 11, 1, 1, 2, 3, 19]
    #     informTime = [0, 540, 347, 586, 0, 748, 824, 486, 0, 777, 0, 202, 653, 713, 454, 0, 0, 0, 574, 735, 721, 772]
    #     expected = 9132
    #     self.t(n, headID, manager, informTime, expected)


    def test11(self):
        n = 1
        headID = 0
        manager = [-1]
        informTime = [0]
        expected = 0
        self.t1(n, headID, manager, informTime, expected)


    def test21(self):
        n = 6
        headID = 2
        manager = [2, 2, -1, 2, 2, 2]
        informTime = [0, 0, 1, 0, 0, 0]
        expected = 1
        self.t1(n, headID, manager, informTime, expected)

    # def test31(self):
    #     n = 22
    #     headID = 7,
    #     manager = [12, 7, 18, 11, 13, 21, 12, -1, 6, 5, 14, 13, 14, 9, 20, 13, 11, 1, 1, 2, 3, 19]
    #     informTime = [0, 540, 347, 586, 0, 748, 824, 486, 0, 777, 0, 202, 653, 713, 454, 0, 0, 0, 574, 735, 721, 772]
    #     expected = 9132
    #     self.t1(n, headID, manager, informTime, expected)


if __name__ == '__main__':
    unittest.main()