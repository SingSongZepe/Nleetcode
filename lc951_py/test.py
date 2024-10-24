import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, root1, root2, expected=None):
        result = Solution1().flipEquiv(root1, root2)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root1 = None
        root2 = None
        expected = True
        self.t(root1, root2, expected)

    def test2(self):
        root1 = None
        root2 = TreeNode(1)
        expected = False
        self.t(root1, root2, expected)

    def test3(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.left.left = TreeNode(4)
        root1.left.right = TreeNode(5)
        root1.left.right.left = TreeNode(7)
        root1.left.right.right = TreeNode(8)

        root1.right = TreeNode(3)
        root1.right.left = TreeNode(6)

        #
        root2 = TreeNode(1)
        root2.left = TreeNode(3)
        root2.left.right = TreeNode(6)

        root2.right = TreeNode(2)
        root2.right.left = TreeNode(4)
        root2.right.right = TreeNode(5)
        root2.right.right.left = TreeNode(8)
        root2.right.right.right = TreeNode(7)

        expected = True
        self.t(root1, root2, expected)

if __name__ == '__main__':
    unittest.main()