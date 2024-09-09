import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().isBalanced(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root = build_tree([3,9,20,None,None,15,7])
        self.t(root, True)

    def test2(self):
        root = build_tree([1,2,2,3,3,None,None,4,4])
        self.t(root, False)

    def test3(self):
        root = build_tree([])
        self.t(root, True)


if __name__ == '__main__':
    unittest.main()