import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().longestZigZag(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        null = None
        root = build_tree([1, 2, null, null, 3, null, null, null, null, 4])
        expected = 3
        self.t(root, expected)


if __name__ == '__main__':
    unittest.main()