import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().reformatDate(arg)
        print(result)
        self.assertEqual(result, expected)

    def test1(self):
        date = '20th Oct 2052'
        expected = '2052-10-20'
        self.t(date, expected)

    def test2(self):
        date = '6th Jun 1933'
        expected = '1933-06-06'
        self.t(date, expected)

    def test3(self):
        date = '26th May 1960'
        expected = '1960-05-26'
        self.t(date, expected)

if __name__ == '__main__':
    unittest.main()