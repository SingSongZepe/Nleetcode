import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, robot, factory, expected=None):
        result = Solution().minimumTotalDistance(robot, factory)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        robot = [0,4,6]
        factory = [[2,2],[6,2]]
        expected = 4
        self.t(robot, factory, expected)

    def test2(self):
        robot = [1,-1]
        factory = [[-2,1],[2,1]]
        expected = 2
        self.t(robot, factory, expected)



if __name__ == '__main__':
    unittest.main()