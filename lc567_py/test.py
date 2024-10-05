import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s1, s2, expected=None):
        result = Solution().checkInclusion(s1, s2)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        s1 = 'ab'
        s2 = 'eidbaooo'
        expected = True
        self.t(s1, s2, expected)

    def test2(self):
        s1 = 'ab'
        s2 = 'eidboaoo'
        expected = False
        self.t(s1, s2, expected)

    def test3(self):
        s1 = 'a'
        s2 = 'ab'
        expected = True
        self.t(s1, s2, expected)

if __name__ == '__main__':
    unittest.main()