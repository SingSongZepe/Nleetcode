import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, current, correct, expected=None):
        result = Solution().convertTime(current, correct)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        current = '02:30'
        correct = '04:35'
        expected = 3
        self.t(current, correct, expected)

    def test2(self):
        current = '11:00'
        correct = '11:01'
        expected = 1
        self.t(current, correct, expected)

if __name__ == '__main__':
    unittest.main()