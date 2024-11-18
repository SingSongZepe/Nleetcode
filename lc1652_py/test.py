import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, code, k, expected=None):
        result = Solution().decrypt(code, k)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        code = [5,7,1,4]
        k = 3
        expected = [12,10,16,13]
        self.t(code, k, expected)

    def test2(self):
        code = [1,2,3,4]
        k = 0
        expected = [0, 0, 0, 0]
        self.t(code, k, expected)

    def test3(self):
        code = [2, 4, 9, 3]
        k = -2
        expected = [12, 5, 6, 13]
        self.t(code, k, expected)

if __name__ == '__main__':
    unittest.main()