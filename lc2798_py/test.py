import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, hours, target, expected=None):
        result = Solution().numberOfEmployeesWhoMetTarget(hours, target)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        hours = [0, 1, 2, 3, 4]
        target = 2
        expected = 3
        self.t(hours, target, expected)

    def test2(self):
        hours = [5, 1, 4, 2, 2]
        target = 6
        expected = 0
        self.t(hours, target, expected)

if __name__ == '__main__':
    unittest.main()