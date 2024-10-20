import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().parseBoolExpr(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().parseBoolExpr(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        expression = '&(|(f))'
        expected = False
        self.t(expression, expected)

    def test2(self):
        expression = '|(f,f,f,t)'
        expected = True
        self.t(expression, expected)

    def test3(self):
        expression = "!(&(f,t))"
        expected = True
        self.t(expression, expected)

    def test4(self):
        expression = "!(&(t,|(f,f,f,t),f))"
        expected = True
        self.t(expression, expected)

    def test5(self):
        expression = "|(&(t,f,t),!(t))"
        expected = False
        self.t(expression, expected)

    def test31(self):
        expression = "!(&(f,t))"
        expected = True
        self.t1(expression, expected)

    def test41(self):
        expression = "!(&(t,|(f,f,f,t),f))"
        expected = True
        self.t1(expression, expected)

    def test51(self):
        expression = "|(&(t,f,t),!(t))"
        expected = False
        self.t1(expression, expected)


if __name__ == '__main__':
    unittest.main()