import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().convertDateToBinary(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        date = '2080-02-29'
        expected = '100000100000-10-11101'
        self.t(date, expected)

    def test2(self):
        date = '1900-01-01'
        expected = '11101101100-1-1'
        self.t(date, expected)

if __name__ == '__main__':
    unittest.main()