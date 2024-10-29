import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, p, i, expected=None):
        result = Solution1().buildTree(p, i)
        print(result)
        self.assertEqual(preorder(result), p)
        self.assertEqual(inoreder(result), i)
        
    def test1(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        self.t(preorder, inorder)

    def test2(self):
        preorder = [-1]
        inorder = [-1]
        self.t(preorder, inorder)

if __name__ == '__main__':
    unittest.main()