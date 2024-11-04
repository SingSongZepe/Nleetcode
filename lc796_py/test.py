import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s, goal, expected=None):
        result = Solution().rotateString(s, goal)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s = "abcde"
        goal = "cdeab"
        expected = True
        self.t(s, goal, expected)

    def test2(self):
        s = "abcde"
        goal = "abced"
        expected = False
        self.t(s, goal, expected)

if __name__ == '__main__':
    unittest.main()