import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().subtractProductAndSum(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 234
        expected = 15
        self.t(n, expected)

    def test2(self):
        n = 4421
        expected = 21
        self.t(n, expected)

if __name__ == '__main__':
    unittest.main()