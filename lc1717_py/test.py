import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maximumGain(*arg)
        print(result)
        
    def test1(self):
        s = "cdbcbbaaabab"
        x = 4
        y = 5
        expected = 19
        self.t([s, x, y], 19)

    def test2(self):
        s = "aabbaaxybbaabb"
        x = 5
        y = 4
        expected = 20
        self.t([s, x, y], expected)

if __name__ == '__main__':
    unittest.main()