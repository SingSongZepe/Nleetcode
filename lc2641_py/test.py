import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().replaceValueInTree(arg)
        print(result)
        
    def test1(self):
        root = TreeNode(5)

        root.left = TreeNode(4)
        root.right = TreeNode(9)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(10)

        root.right.right = TreeNode(7)

        self.t(root)

if __name__ == '__main__':
    unittest.main()