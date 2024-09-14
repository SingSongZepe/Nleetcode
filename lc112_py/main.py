

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node: Optional[TreeNode], target: int) -> bool:
            if node is None:
                return False
            target -= node.val
            if node.left is None and node.right is None:
                return target == 0

            return dfs(node.left, target) or dfs(node.right, target)

        return False if root is None else dfs(root, targetSum)



def build_tree(arr: List[int]) -> Optional[TreeNode]:
    def build_helper(arr: List[int], idx: int) -> Optional[TreeNode]:
        if idx >= len(arr) or arr[idx] is None:
            return None
        node = TreeNode(arr[idx])
        node.left = build_helper(arr, 2 * idx + 1)
        node.right = build_helper(arr, 2 * idx + 2)
        return node

    return build_helper(arr, 0)

def main():

    print('Hello World')

if __name__ == '__main__':
    main()