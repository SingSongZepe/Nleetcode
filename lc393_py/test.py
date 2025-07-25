import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().validUtf8(arg)
        self.assertEqual(result, expected)
        print(result)
        
    def test1(self):
        # 11000101 10000010 00000001.
        data = [197, 130, 1]
        expected = True
        self.t(data, expected)

    def test2(self):
        data = [235, 140, 4]
        expected = False
        self.t(data, expected)

    def test3(self):
        data = [255]
        expected = False
        self.t(data, expected)


if __name__ == '__main__':
    unittest.main()