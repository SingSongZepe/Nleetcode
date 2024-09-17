import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().findMinDifference(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        timePoints = ["23:59","00:00"]
        expected = 1
        self.t(timePoints, expected)

    def test2(self):
        timePoints = ["05:31","22:08","5:35"]
        expected = 4
        self.t(timePoints, expected)

    def test3(self):
        timePoints = ["00:00","23:59","00:00"]
        expected = 0
        self.t(timePoints, expected)

if __name__ == '__main__':
    unittest.main()