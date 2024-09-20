import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, jewels, stones, expected=None):
        result = Solution().numJewelsInStones(jewels, stones)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        jewels = 'aA'
        stones = 'aAAbbbb'
        expected = 3
        self.t(jewels, stones, expected)

    def test2(self):
        jewels = 'z'
        stones = 'ZZ'
        expected = 0
        self.t(jewels, stones, expected)

if __name__ == '__main__':
    unittest.main()