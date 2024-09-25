import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s1, s2, expected=None):
        result = Solution().areAlmostEqual(s1, s2)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s1 = 'bank'
        s2 = 'kanb'
        expected = True
        self.t(s1, s2, expected)

    def test2(self):
        s1 = 'attack'
        s2 = 'defend'
        expected = False
        self.t(s1, s2, expected)

    def test3(self):
        s1 = 'kelb'
        s2 = 'kelb'
        expected = True
        self.t(s1, s2, expected)

    def test4(self):
        s1 = 'kelb'
        s2 = 'celb'
        expected = False
        self.t(s1, s2, expected)

    def test5(self):
        s1 = 'kelb'
        s2 = 'eelk'
        expected = False
        self.t(s1, s2, expected)

if __name__ == '__main__':
    unittest.main()