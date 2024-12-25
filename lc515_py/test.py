import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().largestValues(arg)
        print(result)
        
    def test1(self):
        root = TreeNode(1)

        root.left = TreeNode(3)
        root.right = TreeNode(2)

        root.left.left = TreeNode(5)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(9)

        expected = [1, 3, 9]

        self.t(root, expected)

    def test2(self):
        root = TreeNode(1)

        root.left = TreeNode(2)
        root.right = TreeNode(3)

        expected = [1, 3]

        self.t(root, expected)

if __name__ == '__main__':
    unittest.main()