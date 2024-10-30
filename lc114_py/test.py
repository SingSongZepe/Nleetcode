import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        Solution().flatten(arg)
        print(arg)
        print_list(arg)
        
    def test1(self):
        root = TreeNode(1)

        root.left = TreeNode(2)
        root.right = TreeNode(5)

        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)

        root.right.right = TreeNode(6)

        self.t(root)

if __name__ == '__main__':
    unittest.main()