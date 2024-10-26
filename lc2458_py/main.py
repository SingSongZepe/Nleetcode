

from typing import Optional, List, Set

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        removal = [0] * 100001
        height = [0] * 100001

        #                                           h
        def dfs(node: TreeNode, depth: int = 0) -> int:
            if node.left is None and node.right is None:
                height[node.val] = 1
                return 1
            l = dfs(node.left, depth+1) if node.left else 0
            r = dfs(node.right, depth+1) if node.right else 0

            if node.left:
                removal[node.left.val] = depth + r
            if node.right:
                removal[node.right.val] = depth + l

            height[node.val] = max(l, r) + 1
            return height[node.val]

        dfs(root)

        def update_removal(node: TreeNode, other_side_max: int, depth: int = 0):
            if node.left is None and node.right is None:
                return

            if node.left:
                removal[node.left.val] = max(removal[node.left.val], other_side_max)
                update_removal(node.left, max(height[node.right.val] + depth + 1, other_side_max) if node.right else other_side_max, depth + 1)
            if node.right:
                removal[node.right.val] = max(removal[node.right.val], other_side_max)
                update_removal(node.right, max(height[node.left.val] + depth + 1, other_side_max) if node.left else other_side_max, depth + 1)

        right_side_max = height[root.right.val] if root.right else 0
        if root.left:
            update_removal(root.left, right_side_max)
        left_side_max = height[root.left.val] if root.left else 0
        if root.right:
            update_removal(root.right, left_side_max)

        res = []
        for query in queries:
            res.append(removal[query])

        return res


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        removal = {}
        height = {}

        #                                           h
        def dfs(node: TreeNode, depth: int = 0) -> int:
            if node.left is None and node.right is None:
                height[node.val] = 1
                return 1
            l = dfs(node.left, depth+1) if node.left else 0
            r = dfs(node.right, depth+1) if node.right else 0

            if node.left:
                removal[node.left.val] = depth + r
            if node.right:
                removal[node.right.val] = depth + l

            height[node.val] = max(l, r) + 1
            return height[node.val]

        dfs(root)

        def update_removal(node: TreeNode, other_side_max: int, depth: int = 0):
            if node.left is None and node.right is None:
                return

            if node.left:
                removal[node.left.val] = max(removal[node.left.val], other_side_max)
                update_removal(node.left, max(height[node.right.val] + depth + 1, other_side_max) if node.right else other_side_max, depth + 1)
            if node.right:
                removal[node.right.val] = max(removal[node.right.val], other_side_max)
                update_removal(node.right, max(height[node.left.val] + depth + 1, other_side_max) if node.left else other_side_max, depth + 1)

        right_side_max = height[root.right.val] if root.right else 0
        if root.left:
            update_removal(root.left, right_side_max)
        left_side_max = height[root.left.val] if root.left else 0
        if root.right:
            update_removal(root.right, left_side_max)

        res = []
        for query in queries:
            res.append(removal[query])

        return res

def main():
    print('Hello World')

if __name__ == '__main__':
    main()