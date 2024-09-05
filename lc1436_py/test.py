import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().destCity(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
        expected = "Sao Paulo"
        self.t(paths, expected)

    def test2(self):
        paths = [["B","C"],["D","B"],["C","A"]]
        expected = "A"
        self.t(paths, expected)

    def test3(self):
        paths = [["A","Z"]]
        expected = "Z"
        self.t(paths, expected)


if __name__ == '__main__':
    unittest.main()