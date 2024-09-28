import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, startTime, endTime, queryTime, expected=None):
        result = Solution().busyStudent(startTime, endTime, queryTime)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        startTime = [1, 2, 3]
        endTime = [3, 2, 7]
        queryTime = 4
        expected = 1
        self.t(startTime, endTime, queryTime, expected)

    def test2(self):
        startTime = [4]
        endTime = [4]
        queryTime = 4
        expected = 1
        self.t(startTime, endTime, queryTime, expected)



if __name__ == '__main__':
    unittest.main()