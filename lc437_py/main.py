

from typing import Optional, List, Dict
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        tot = 0
        def dfs(node: Optional[TreeNode], path_psum: Dict[int, int]) -> None:
            if node is None:
                return

            path_psum = {k+node.val: v for k, v in path_psum.items()}
            if node.val in path_psum:
                path_psum[node.val] += 1
            else:
                path_psum[node.val] = 1

            nonlocal tot
            if targetSum in path_psum:
                tot += path_psum[targetSum]

            dfs(node.left, path_psum)
            dfs(node.right, path_psum)

        dfs(root, defaultdict(int))

        return tot


class Solution1:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        psum: Dict[int, int] = defaultdict(int)
        psum[0] += 1
        tot = 0

        def dfs(node: Optional[TreeNode], csum: int):
            if node is None:
                return

            csum += node.val

            nonlocal tot
            diff = csum - targetSum
            if diff in psum:
                tot += psum[diff]

            psum[csum] += 1

            if node.left:
                dfs(node.left, csum)
                psum[csum + node.left.val] -= 1

            if node.right:
                dfs(node.right, csum)
                psum[csum + node.right.val] -= 1

        dfs(root, 0)
        return tot


def main():
    print('Hello World')

if __name__ == '__main__':
    main()