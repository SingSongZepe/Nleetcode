

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def g(node, depth) -> Optional[int]:
            if not node:
                return 100001
            if not node.left and not node.right:
                return depth
            return min(g(node.left, depth + 1), g(node.right, depth + 1))

        return g(root, 1)


from collections import deque

# BFS
class Solution1:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minDepth = float('inf')
        if not root:
            return 0
        queue = deque()
        queue.append((root, 1))
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))


class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minDepth = float('inf')
        if not root:
            return 0
        queue = deque([root])
        level = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    minDepth = min(minDepth, level)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return minDepth

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