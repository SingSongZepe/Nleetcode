import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, k, expected=None):
        result = Solution().canArrange(arg, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        arr = [1,2,3,4,5,10,6,7,8,9]
        k = 5
        expected = True
        self.t(arr, k, expected)

    def test2(self):
        arr = [1, 2, 3, 4, 5, 6]
        k = 7
        expected = True
        self.t(arr, k, expected)

    def test3(self):
        arr = [1, 2, 3, 4, 5, 6]
        k = 10
        expected = False
        self.t(arr, k, expected)


if __name__ == '__main__':
    unittest.main()