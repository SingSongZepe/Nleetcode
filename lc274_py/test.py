import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().hIndex(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        citation = [3, 0, 6, 1, 5]
        expected = 3
        self.t(citation, expected)

    def test2(self):
        citations = [1, 3, 1]
        expected = 1
        self.t(citations, expected)

if __name__ == '__main__':
    unittest.main()