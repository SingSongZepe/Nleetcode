import unittest
from main import *


class Test(unittest.TestCase):
    def t(self, root, targetSum, expected=None):
        result = Solution().hasPathSum(root, targetSum)
        print(result)
        self.assertEqual(result, expected)
        
    def test1(self):
        root = build_tree([1, 2, 3])
        targetSum = 5
        expected = False
        self.t(root, targetSum, expected)

    def test2(self):
        root = build_tree([])
        targetSum = 0
        expected = False
        self.t(root, targetSum, expected)

    def test3(self):
        root = build_tree([1, 2])
        targetSum = 1
        expected = False
        self.t(root, targetSum, expected)

if __name__ == '__main__':
    unittest.main()