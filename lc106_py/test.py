import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, i, p, expected=None):
        result = Solution().buildTree(i, p)
        print(result)
        self.assertEqual(inoreder(result), i)
        self.assertEqual(postoreder(result), p)
        
    def test1(self):
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        self.t(inorder, postorder)

    def test2(self):
        inorder = [-1]
        postorder = [-1]
        self.t(inorder, postorder)


if __name__ == '__main__':
    unittest.main()