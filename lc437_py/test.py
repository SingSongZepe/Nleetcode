import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, root, ts, expected=None):
        result = Solution().pathSum(root, ts)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root = TreeNode(10)

        root.left = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right = TreeNode(2)
        root.left.right.right = TreeNode(1)

        root.right = TreeNode(-3)
        root.right.right = TreeNode(11)

        targetSum = 8
        expected = 3
        self.t(root, targetSum, expected)

    def test2(self):
        root = TreeNode(1)

        targetSum = 1
        expected = 1
        self.t(root, targetSum, expected)

    def test3(self):
        root = TreeNode(1)

        root.left = TreeNode(-2)
        root.left.left = TreeNode(1)
        root.left.left.left = TreeNode(-1)
        root.left.right = TreeNode(3)

        root.right = TreeNode(-3)
        root.right.left = TreeNode(-2)

        targetSum = 0
        expected = 2
        self.t(root, targetSum, expected)



if __name__ == '__main__':
    unittest.main()