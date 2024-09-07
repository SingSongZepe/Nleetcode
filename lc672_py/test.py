import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, n, presses, expected=None):
        result = Solution().flipLights(n, presses)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        n = 1
        presses = 1
        expected = 2
        self.t(n, presses, expected)

    def test2(self):
        n = 2
        presses = 1
        expected = 3
        self.t(n, presses, expected)

    def test3(self):
        n = 3
        presses = 1
        expected = 4
        self.t(n, presses, expected)


if __name__ == '__main__':
    unittest.main()