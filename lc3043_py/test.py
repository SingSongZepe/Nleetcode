import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arr1, arr2, expected=None):
        result = Solution().longestCommonPrefix(arr1, arr2)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        arr1 = [1, 10, 100]
        arr2 = [1000]
        expected = 3
        self.t(arr1, arr2, expected)

    def test2(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 4, 4]
        expected = 0
        self.t(arr1, arr2, expected)


    def test3(self):
        arr1 = [1, 2, 3, 5123]
        arr2 = [4, 4, 4, 5]
        expected = 1
        self.t(arr1, arr2, expected)

if __name__ == '__main__':
    unittest.main()