import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().diffWaysToCompute(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        expression = '2-1-1'
        expected = [0, 2]
        self.t(expression, expected)

    def test2(self):
        expression = '2*3-4*5'
        expected = [-34, -14, -10, -10, 10]
        self.t(expression, expected)


if __name__ == '__main__':
    unittest.main()