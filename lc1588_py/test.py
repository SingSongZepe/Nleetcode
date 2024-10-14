import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().sumOddLengthSubarrays(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution().sumOddLengthSubarrays(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        arr = [1, 4, 2, 5, 3]
        expected = 58
        self.t(arr, expected)

    def test2(self):
        arr = [1, 2]
        expected = 3
        self.t(arr, expected)

    def test3(self):
        arr = [10, 11, 12]
        expected = 66
        self.t(arr, expected)

    def test11(self):
        arr = [1, 4, 2, 5, 3]
        expected = 58
        self.t1(arr, expected)

    def test21(self):
        arr = [1, 2]
        expected = 3
        self.t1(arr, expected)

    def test31(self):
        arr = [10, 11, 12]
        expected = 66
        self.t1(arr, expected)

if __name__ == '__main__':
    unittest.main()