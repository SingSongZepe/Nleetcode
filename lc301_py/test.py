import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().removeInvalidParentheses(arg)
        print(result)
        st = set(expected)
        if not result:
            self.fail(f"Expected {expected}, but got {result}")

        if set(result) == set(expected):
            self.assertTrue(True)
        else:
            self.fail(f"Expected {expected}, but got {result}")

        print('Test passed')

    def t1(self, arg, expected=None):
        result = Solution1().removeInvalidParentheses(arg)
        print(result)
        st = set(expected)
        if not result:
            self.fail(f"Expected {expected}, but got {result}")

        if set(result) == set(expected):
            self.assertTrue(True)
        else:
            self.fail(f"Expected {expected}, but got {result}")

        print('Test passed')
        
    def test1(self):
        s = '()())()'
        expected = ['()()()', '(())()']
        self.t(s, expected)

    def test2(self):
        s = '(a)())()'
        expected = ['(a)()()', '(a())()']
        self.t(s, expected)

    def test3(self):
        s = ')('
        expected = ['']
        self.t(s, expected)

    def test4(self):
        s = "(((k()(("
        expected = ["k()","(k)"]
        self.t(s, expected)


    def test11(self):
        s = '()())()'
        expected = ['()()()', '(())()']
        self.t1(s, expected)

    def test21(self):
        s = '(a)())()'
        expected = ['(a)()()', '(a())()']
        self.t1(s, expected)

    def test31(self):
        s = ')('
        expected = ['']
        self.t1(s, expected)

    def test41(self):
        s = "(((k()(("
        expected = ["k()","(k)"]
        self.t1(s, expected)



if __name__ == '__main__':
    unittest.main()