import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().maxNumberOfBalloons(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        text = 'nlaebolko'
        expected = 1
        self.t(text, expected)

    def test2(self):
        text = 'loonbalxballpoon'
        expected = 2
        self.t(text, expected)

    def test3(self):
        text = 'leetcode'
        expected = 0
        self.t(text, expected)


if __name__ == '__main__':
    unittest.main()