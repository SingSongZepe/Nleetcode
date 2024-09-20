import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().rankTeams(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        votes = ["ABC","ACB","ABC","ACB","ACB"]
        expected = "ACB"
        self.t(votes, expected)

    def test2(self):
        votes = ["WXYZ","XYZW"]
        expected = "XWYZ"
        self.t(votes, expected)

    def test3(self):
        votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
        expected = "ZMNAGUEDSJYLBOPHRQICWFXTVK"
        self.t(votes, expected)


if __name__ == '__main__':
    unittest.main()