import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, amount, coins, expected=None):
        result = Solution().change(amount, coins)
        print(result)
        
    def test1(self):
        amount = 5
        coins = [1, 2, 5]
        expected = 4
        self.t(amount, coins, expected)

    def test2(self):
        amount = 3
        coins = [2]
        expected = 0
        self.t(amount, coins, expected)

    def test3(self):
        amount = 10
        coins = [10]
        expected = 1
        self.t(amount, expected)

if __name__ == '__main__':
    unittest.main()