import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().minDepth(arg)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, arg, expected=None):
        result = Solution1().minDepth(arg)
        print(result)
        self.assertEqual(result, expected)

    def t2(self, arg, expected=None):
        result = Solution1().minDepth(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root = build_tree([3,9,20,None,None,15,7])
        expected = 2
        self.t(root, expected)

    def test2(self):
        root = build_tree([3,9,None,1])
        expected = 3
        self.t(root, expected)

    def test3(self):
        root = build_tree([3,9,None,1])
        expected = 3
        self.t(root, expected)


    def test11(self):
        root = build_tree([3,9,20,None,None,15,7])
        expected = 2
        self.t1(root, expected)

    def test21(self):
        root = build_tree([3,9,None,1])
        expected = 3
        self.t1(root, expected)

    def test31(self):
        root = build_tree([3,9,None,1])
        expected = 3
        self.t1(root, expected)


    def test12(self):
        root = build_tree([3,9,20,None,None,15,7])
        expected = 2
        self.t2(root, expected)

    def test22(self):
        root = build_tree([3,9,None,1])
        expected = 3
        self.t2(root, expected)

    def test32(self):
        root = build_tree([3,9,None,1])
        expected = 3
        self.t2(root, expected)

if __name__ == '__main__':
    unittest.main()