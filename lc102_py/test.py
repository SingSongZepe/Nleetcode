import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().levelOrder(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root = TreeNode(3)

        root.left = TreeNode(9)
        root.right = TreeNode(20)

        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        expected = [[3],[9,20],[15,7]]

        self.t(root, expected)

if __name__ == '__main__':
    unittest.main()