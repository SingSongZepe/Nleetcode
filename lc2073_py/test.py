import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, tickets, k, expected=None):
        result = Solution().timeRequiredToBuy(tickets, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        tickets = [5, 1, 1, 1]
        k = 0
        expected = 8
        self.t(tickets, k, expected)

    def test2(self):
        tickets = [2,3,2]
        k = 2
        expected = 6
        self.t(tickets, k, expected)

if __name__ == '__main__':
    unittest.main()