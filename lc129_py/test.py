import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().sumNumbers(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root = TreeNode(1)

        root.left = TreeNode(2)
        root.right = TreeNode(3)

        expected = 25
        self.t(root, expected)

    def test2(self):
        root = TreeNode(4)

        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)

        expected = 1026
        self.t(root, expected)

if __name__ == '__main__':
    unittest.main()