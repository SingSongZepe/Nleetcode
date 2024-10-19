import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arr, m, k, expected=None):
        result = Solution().containsPattern(arr, m, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        arr = [1, 2, 4, 4, 4, 4]
        m = 1
        k = 3
        expected = True
        self.t(arr, m, k, expected)

    def test2(self):
        arr = [1, 2, 1, 2, 1, 1, 1, 3]
        m = 2
        k = 2
        expected = True
        self.t(arr, m, k, expected)

    def test3(self):
        arr = [1, 2, 1, 2, 1, 3]
        m = 2
        k = 3
        expected = False
        self.t(arr, m, k, expected)


if __name__ == '__main__':
    unittest.main()