


from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def g(start, end) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                left_trees = g(start, i-1)
                right_trees = g(i+1, end)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        return g(1, n)

class Solution1:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        dp = {}

        def g(start, end) -> List[Optional[TreeNode]]:
            if (start, end) in dp:
                return dp[(start, end)]
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                left_trees = g(start, i-1)
                right_trees = g(i+1, end)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i, l, r)
                        res.append(root)
            dp[(start, end)] = res
            return res

        return g(1, n)

def main():
    print('Hello World')

if __name__ == '__main__':
    main()