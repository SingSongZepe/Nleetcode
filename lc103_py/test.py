import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().zigzagLevelOrder(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root = TreeNode(3)

        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        expected = [[3],[20,9],[15,7]]

        self.t(root, expected)

    def test2(self):
        root = TreeNode(1)

        root.left = TreeNode(2)
        root.right = TreeNode(3)

        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)

        expected = [[1],[3, 2],[4,5]]

        self.t(root, expected)



if __name__ == '__main__':
    unittest.main()