import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().getRow(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        rowIndex = 3
        expected = [1, 3, 3, 1]
        self.t(rowIndex, expected)

    def test2(self):
        rowIndex = 0
        expected = [1]
        self.t(rowIndex, expected)

    def test3(self):
        rowIndex = 1
        expected = [1, 1]
        self.t(rowIndex, expected)

    def test4(self):
        rowIndex = 5
        expected = [1, 5, 10, 10, 5, 1]
        self.t(rowIndex, expected)

if __name__ == '__main__':
    unittest.main()