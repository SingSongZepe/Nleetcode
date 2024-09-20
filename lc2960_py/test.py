import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().countTestedDevices(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        batteryPercentages = [1, 1, 2, 1, 3]
        expected = 3
        self.t(batteryPercentages, expected)

    def test2(self):
        batteryPercentages = [0, 1, 2]
        expected = 2
        self.t(batteryPercentages, expected)

if __name__ == '__main__':
    unittest.main()