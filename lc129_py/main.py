

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        tot = 0
        curr = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal curr, tot

            curr = 10 * curr + node.val
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            if not (node.left or node.right):
                tot += curr
            curr //= 10

        dfs(root)
        return tot






def main():
    print('Hello World')

if __name__ == '__main__':
    main()