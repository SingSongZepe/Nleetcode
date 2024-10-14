import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().sumSubarrayMins(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        arr = [3, 1, 2, 4]
        expected = 17
        self.t(arr, expected)

    def test2(self):
        arr = [11, 81, 94, 43, 3]
        expected = 444
        self.t(arr, expected)

    def test3(self):
        arr = [1, 1]
        expected = 3
        self.t(arr, expected)

if __name__ == '__main__':
    unittest.main()