import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, ts, expected=None):
        result = Solution().pathSum(arg, ts)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root = TreeNode(1)

        root.left = TreeNode(2)
        root.right = TreeNode(3)

        ts = 5

        expected = []
        self.t(root, ts, expected)

    def test2(self):
        root = TreeNode(5)

        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)

        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)

        ts = 22

        expected = [[5,4,11,2],[5,8,4,5]]
        self.t(root, ts, expected)

if __name__ == '__main__':
    unittest.main()