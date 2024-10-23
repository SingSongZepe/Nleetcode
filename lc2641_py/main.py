

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        lvl_sum = []

        def dfs_count(n: TreeNode, lvl: int):
            if len(lvl_sum) > lvl:
                lvl_sum[lvl] += n.val
            else:
                lvl_sum.append(n.val)

            if n.left:
                dfs_count(n.left, lvl+1)
            if n.right:
                dfs_count(n.right, lvl+1)

        def dfs_replace(n: TreeNode, lvl: int):

            if n.left and n.right:
                n.left.val = n.right.val = lvl_sum[lvl] - n.left.val - n.right.val
                dfs_replace(n.left, lvl+1)
                dfs_replace(n.right, lvl+1)
            elif n.left:
                n.left.val = lvl_sum[lvl] - n.left.val
                dfs_replace(n.left, lvl+1)
            elif n.right:
                n.right.val = lvl_sum[lvl] - n.right.val
                dfs_replace(n.right, lvl+1)

        dfs_count(root, 0)
        root.val = 0
        dfs_replace(root, 1)

        return root















        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()