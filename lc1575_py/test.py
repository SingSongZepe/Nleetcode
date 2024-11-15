import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, locations, start, finish, fuel, expected=None):
        result = Solution().countRoutes(locations, start, finish, fuel)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        locations = [2,3,6,8,4]
        start = 1
        finish = 3
        fuel = 5
        expected = 4
        self.t(locations, start, finish, fuel, expected)

    def test2(self):
        locations = [4,3,1]
        start = 1
        finish = 0
        fuel = 6
        expected = 5
        self.t(locations, start, finish, fuel, expected)


if __name__ == '__main__':
    unittest.main()