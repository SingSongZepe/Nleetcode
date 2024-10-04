import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().dividePlayers(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().dividePlayers(arg)
        print(result)
        self.assertEqual(result, expected)


    def test1(self):
        skill = [3, 2, 5, 1, 3, 4]
        expected = 22
        self.t(skill, expected)

    def test2(self):
        skill = [3, 4]
        expected = 12
        self.t(skill, expected)

    def test3(self):
        skill = [1, 1, 2, 3]
        expected = -1
        self.t(skill, expected)

    def test4(self):
        skill = [1, 1000]
        expected = 1000
        self.t(skill, expected)

    def test5(self):
        skill = [4,4,2,4,4,5]
        expected = -1
        self.t(skill, expected)

    def test6(self):
        skill = [4,4,1,4,4,5]
        expected = -1
        self.t(skill, expected)


    def test11(self):
        skill = [3, 2, 5, 1, 3, 4]
        expected = 22
        self.t1(skill, expected)

    def test21(self):
        skill = [3, 4]
        expected = 12
        self.t1(skill, expected)

    def test31(self):
        skill = [1, 1, 2, 3]
        expected = -1
        self.t1(skill, expected)


if __name__ == '__main__':
    unittest.main()