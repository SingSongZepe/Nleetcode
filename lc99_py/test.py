import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        Solution1().recoverTree(arg)
        print(morris_inorder_traversal(arg))
        
    def test1(self):
        root = build_tree([1,3,None,None,2])
        self.t(root)


    def test_inorder_traversal(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(5)
        print(inorder_traversal(root))

    def test_inorder_traversal1(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(5)
        print(inorder_traversal1(root))


    def test_morris_inorder_traversal(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(5)
        print(morris_inorder_traversal(root))


if __name__ == '__main__':
    unittest.main()