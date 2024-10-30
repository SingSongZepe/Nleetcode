import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, arg, expected=None):
        result = Solution().connect(arg)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root = Node(1)

        root.left = Node(2)
        root.right = Node(3)

        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        self.t(root)



if __name__ == '__main__':
    unittest.main()