import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, rolls, mean, n, expected=None):
        result = Solution().missingRolls(rolls, mean, n)
        print(result)
        # self.assertEqual(result, expected)


    def test1(self):
        rolls = [3, 2, 4, 3]
        mean = 4
        n = 2
        # expected = [6, 6]
        self.t(rolls, mean, n, )

    def test2(self):
        rolls = [1, 5, 6]
        mean = 3
        n = 4
        # expected = [2, 3, 4, 5]
        self.t(rolls, mean, n, )

    def test3(self):
        rolls = [1, 2, 3, 4]
        mean = 6
        n = 4
        self.t(rolls, mean, n, )


if __name__ == '__main__':
    unittest.main()