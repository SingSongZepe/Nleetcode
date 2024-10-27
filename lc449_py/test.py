import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, root, expected=None):

        ser = Codec()
        deser = Codec()
        tree = ser.serialize(root)
        ans = deser.deserialize(tree)

        print(tree)
        print(ans)
        
    def test1(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.t(root)

    def test2(self):
        root = TreeNode(4)

        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        root.right = TreeNode(5)

        self.t(root)


if __name__ == '__main__':
    unittest.main()