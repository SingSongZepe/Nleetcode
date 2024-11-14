import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, n, quantities, expected=None):
        result = Solution().minimizedMaximum(n, quantities)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 6
        quantities = [11, 6]
        expected = 3
        self.t(n, quantities, expected)

    def test2(self):
        n = 7
        quantities = [15, 10, 10]
        expected = 5
        self.t(n, quantities, expected)

    def test3(self):
        n = 1
        quantities = [100000]
        expected = 100000
        self.t(n, quantities, expected)

    def test4(self):
        n = 2
        quantities = [5, 7]
        expected = 7
        self.t(n, quantities, expected)

    def test5(self):
        n = 22
        quantities = [25,11,29,6,24,4,29,18,6,13,25,30]
        expected = 13
        self.t(n, quantities, expected)

    def test6(self):
        n = 26
        quantities = [24,18,12,6,3,24,5,19,10,20,2,18,27,3,13,22,11,16,19,13]
        expected = 19
        self.t(n, quantities, expected)

if __name__ == '__main__':
    unittest.main()