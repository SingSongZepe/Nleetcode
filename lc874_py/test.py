import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, commands, obstacles, expected=None):
        result = Solution().robotSim(commands, obstacles)
        print(result)

    def test1(self):
        commands = [4, -1, 3]
        obstacles = []
        expected = 25
        self.t(commands, obstacles, expected)

    def test2(self):
        commands = [4, -1, 4, -2, 4]
        obstacles = [[2, 4]]
        expected = 65
        self.t(commands, obstacles, expected)

    def test3(self):
        commands = [6, -1, -1, 6]
        obstacle = []
        expected = 36
        self.t(commands, obstacle, expected)

    def test4(self):
        commands = [1,-1,1,-1,1,-1,6]
        obstacles = [[0,0]]
        expected = 2
        self.t(commands, obstacles, expected)


    # up test
    def test5(self):
        commands = [5]
        obstacles = [[0, 2]]
        expected = 1
        self.t(commands, obstacles, expected)

    # down test
    def test6(self):
        commands = [-2, -2, 4]
        obstacles = [[0, 2]]
        expected = 1
        self.t(commands, obstacles, expected)



    # test bs
    def test_bs(self):
        arr = [1,3, 10, 15, 30, 55, 100]
        n = 29
        b = Solution().bs_greater_than(arr, n)
        print(b)

    def test_bs2(self):
        arr = [1,3, 10, 15, 30, 55, 100]
        n = 30
        b = Solution().bs_less_than(arr, n)
        print(b)

if __name__ == '__main__':
    unittest.main()