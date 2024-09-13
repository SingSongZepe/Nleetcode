import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().generateTrees(arg)
        # print(result)
        print(len(result))
        # self.assertEqual(result, expected)
        
    def test1(self):
        n = 3
        self.t(n)

    def test2(self):
        n = 1
        self.t(n)

    def test3(self):
        n = 8
        self.t(n)

    def test4(self):
        n = 10
        self.t(n)

    def test5(self):
        n = 12
        self.t(n)

    def test6(self):
        n = 13
        self.t(n)

    def test7(self):
        n = 14
        self.t(n)

    def test8(self):
        n = 15
        self.t(n)

if __name__ == '__main__':
    unittest.main()