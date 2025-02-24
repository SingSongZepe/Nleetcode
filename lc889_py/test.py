import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, preorder, postorder, expected=None):
        result = Solution().constructFromPrePost(preorder, postorder)
        print(result)

    def test1(self):
        preorder = [1,2,4,5,3,6,7]
        postorder = [4,5,2,6,7,3,1]

        self.t(preorder, postorder)

    def test2(self):
        preorder =  [1, 2]
        postorder = [2, 1]

        self.t(preorder, postorder)

if __name__ == '__main__':
    unittest.main()