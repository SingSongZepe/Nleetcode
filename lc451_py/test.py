import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().frequencySort(arg)
        print(result)
        # self.assertEqual(result, expected)
        
    def test1(self):
        s = 'tree'
        expected = 'eert'
        self.t(s, expected)

    def test2(self):
        s = 'cccaaa'
        expected = 'aaaccc'
        self.t(s, expected)

    def test3(self):
        s = 'Aabb'
        expected = 'bbAa'
        self.t(s, expected)


if __name__ == '__main__':
    unittest.main()