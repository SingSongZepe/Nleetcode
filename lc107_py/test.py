import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().levelOrderBottom(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root = TreeNode(3)

        root.left = TreeNode(9)
        root.right = TreeNode(20)

        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        expected = [[15,7],[9,20],[3]]

        self.t(root, expected)

if __name__ == '__main__':
    unittest.main()