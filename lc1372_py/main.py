

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        # dir, True for left to right, False for right to left
        def dfs(node: Optional[TreeNode], len: int, dir: bool) -> int:
            if not node:
                return len - 1

            return max(dfs(node.left, len+1 if dir else 1, False), dfs(node.right, len+1 if not dir else 1, True))

        return max(dfs(root.left, 1, False), dfs(root.right, 1, True))


class Solution1:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], dir: str, length: int) -> int:
            if not node:
                return length - 1

            left_length = dfs(node.left, "left", length + 1 if dir == "right" else 1)
            right_length = dfs(node.right, "right", length + 1 if dir == "left" else 1)

            # if dir == "right":
            #     left_length = dfs(node.left, "left", length + 1)
            #     right_length = dfs(node.right, "right", 1)
            # else:
            #     left_length = dfs(node.left, "left", 1)
            #     right_length = dfs(node.right, "right", length + 1)

            return max(left_length, right_length)

        if not root:
            return 0

        return max(dfs(root.left, "left", 1), dfs(root.right, "right", 1))

class Solution2:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxLen = 0

        def dfs(node, dir, len):
            if not node: return

            nonlocal maxLen
            maxLen = max(maxLen, len)

            dfs(node.left, "left", len + 1 if dir == "right" else 1)
            dfs(node.right, "right", len + 1 if dir == "left" else 1)

        if not root: return maxLen
        dfs(root.left, "left", 1)
        dfs(root.right, "right", 1)
        return maxLen


def build_tree(arr: List[int]) -> Optional[TreeNode]:
    def build_helper(i: int) -> Optional[TreeNode]:
        if i >= len(arr) or arr[i] is None:
            return None
        node = TreeNode(arr[i])
        node.left = build_helper(2*i+1)
        node.right = build_helper(2*i+2)
        return node
    return build_helper(0)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()