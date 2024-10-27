import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, root, key, expected=None):
        result = Solution().deleteNode(root, key)
        print(result)
        self.assertEqual(preorder(result), expected)
        
    def test1(self):
        root = TreeNode(5)

        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)

        root.right = TreeNode(6)
        root.right.right = TreeNode(7)

        key = 3

        expected = [5, 4, 2, 6, 7]

        self.t(root, key, expected)

    def test2(self):
        root = TreeNode(5)

        root.left = TreeNode(2)
        root.left.right = TreeNode(4)

        root.right = TreeNode(6)
        root.right.right = TreeNode(7)

        key = 0

        expected = [5, 2, 4, 6, 7]

        self.t(root, key, expected)

    def test3(self):
        root = None

        key = 0

        expected = []

        self.t(root, key, expected)

    def test4(self):
        root = TreeNode(0)

        key = 0

        expected = []

        self.t(root, key, expected)

    def test_tree_reference(self):
        test_tree_reference()


if __name__ == '__main__':
    unittest.main()