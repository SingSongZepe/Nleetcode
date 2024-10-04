import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().calculate(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().calculate(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = '3+2*2'
        expected = 7
        self.t(s, expected)

    def test2(self):
        s = ' 3/2 '
        expected = 1
        self.t(s, expected)

    def test3(self):
        s = ' 3+5 / 2 '
        expected = 5
        self.t(s, expected)

    def test4(self):
        s = ' 4/2 + 1*3*9 - 10 '
        expected = 19
        self.t(s, expected)

    # def test5(self):
    #     s = '1-1+1'
    #     expected = 1
    #     self.t(s, expected)

    def test11(self):
        s = '3+2*2'
        expected = 7
        self.t1(s, expected)

    def test21(self):
        s = ' 3/2 '
        expected = 1
        self.t1(s, expected)

    def test31(self):
        s = ' 3+5 / 2 '
        expected = 5
        self.t1(s, expected)

    def test41(self):
        s = ' 4/2 + 1*3*9 - 10 '
        expected = 19
        self.t1(s, expected)

    def test51(self):
        s = '1-1+1'
        expected = 1
        self.t1(s, expected)

if __name__ == '__main__':
    unittest.main()