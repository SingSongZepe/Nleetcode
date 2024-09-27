import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, s1, s2, expected=None):
        result = Solution().minimumDeleteSum(s1, s2)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        s1 = 'sea'
        s2 = 'eat'
        expected = 231
        self.t(s1, s2, expected)

    def test2(self):
        s1 = 'delete'
        s2 = 'leet'
        expected = 403
        self.t(s1, s2, expected)

if __name__ == '__main__':
    unittest.main()