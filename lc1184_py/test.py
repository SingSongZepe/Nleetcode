import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, distance, start, destination, expected=None):
        result = Solution().distanceBetweenBusStops(distance, start, destination)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        distance = [1,2,3,4]
        start = 0
        destination = 1
        expected = 1
        self.t(distance, start, destination, expected)

    def test2(self):
        distance = [1,2,3,4]
        start = 0
        destination = 2
        expected = 3
        self.t(distance, start, destination, expected)

    def test3(self):
        distance = [1,2,3,4]
        start = 0
        destination = 3
        expected = 4
        self.t(distance, start, destination, expected)

if __name__ == '__main__':
    unittest.main()