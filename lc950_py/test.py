import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().deckRevealedIncreasing(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        deck = [17, 13, 11, 2, 3, 5, 7]
        expected = [2, 13, 3, 11, 5, 17, 7]
        self.t(deck, expected)

    def test2(self):
        deck = [1, 1000]
        expected = [1, 1000]
        self.t(deck, expected)


if __name__ == '__main__':
    unittest.main()