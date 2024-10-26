import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, root, queries, expected=None):
        result = Solution().treeQueries(root, queries)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root = TreeNode(1)

        root.left = TreeNode(3)
        root.left.left = TreeNode(2)

        root.right = TreeNode(4)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(5)
        root.right.right.right = TreeNode(7)

        queries = [4]
        expected = [2]
        self.t(root, queries, expected)

    def test2(self):
        root = TreeNode(5)

        root.left = TreeNode(8)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(1)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(6)

        root.right = TreeNode(9)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(7)

        queries = [3, 2, 4, 8]
        expected = [3, 2, 3, 2]
        self.t(root, queries, expected)

    def test3(self):
        root = TreeNode(1)

        root.right = TreeNode(5)
        root.right.left = TreeNode(3)

        root.right.left.left = TreeNode(2)
        root.right.left.right = TreeNode(4)

        queries = [3, 5, 4, 2, 4]
        expected = [1, 0, 3, 3, 3]
        self.t(root, queries, expected)

    def test4(self):
        root = TreeNode(5)

        root.left = TreeNode(4)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        root.left.left.right = TreeNode(3)

        root.right = TreeNode(6)
        root.right.right = TreeNode(8)
        root.right.right.left = TreeNode(7)

        queries = [8]
        expected = [3]
        self.t(root, queries, expected)


if __name__ == '__main__':
    unittest.main()