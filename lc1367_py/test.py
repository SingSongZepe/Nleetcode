import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, head, root, expected=None):
        result = Solution().isSubPath(head, root)
        print(result)
        self.assertEqual(result, expected)

    def t1(self, head, root, expected=None):
        result = Solution1().isSubPath(head, root)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        head = build_list([1,4,2,6])
        root = build_tree([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
        self.t(head, root, True)

    def test11(self):
        head = build_list([1,4,2,6])
        root = build_tree([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
        self.t1(head, root, True)

    def test3(self):
        head = build_list([1, 2])
        root = build_tree([1, 3, 1, None, None, None, 2])
        self.t(head, root, True)


    def test31(self):
        head = build_list([1, 2])
        root = build_tree([1, 3, 1, None, None, None, 2])
        self.t1(head, root, True)





    def test_build_list(self):
        head = [4, 2, 8]
        list = build_list(head)
        print_list(list)

    def test_build_tree(self):
        root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]
        tree = build_tree(root)
        print(tree)


if __name__ == '__main__':
    unittest.main()