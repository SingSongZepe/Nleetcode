import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().hIndex(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        citations = [0, 1, 3, 5, 6]
        expected = 3
        self.t(citations, expected)

    def test2(self):
        citations = [0, 2, 100]
        expected = 2
        self.t(citations, expected)

if __name__ == '__main__':
    unittest.main()