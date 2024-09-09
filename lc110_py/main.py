
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> List:
            if not node:
                return [True, 0]
            l, r = dfs(node.left), dfs(node.right)
            b = (l[0] and r[0] and abs(l[1] - r[1]) <= 1)
            return [b, 1 + max(l[1], r[1])]
        return dfs(root)[0]


class Solution1:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(Node):
            if Node == None: return 0

            lh = check(Node.left)
            rh = check(Node.right)
            if lh == -1 or rh == -1: return -1
            if abs(lh - rh) > 1: return -1

            return max(lh, rh) + 1

        if check(root) == -1: return False

        return True

def build_tree(arr: List[int]) -> Optional[TreeNode]:

    def build(arr: List[int], idx: int) -> Optional[TreeNode]:
        if idx >= len(arr) or arr[idx] == None:
            return None
        node = TreeNode(arr[idx])
        node.left = build(arr, 2*idx+1)
        node.right = build(arr, 2*idx+2)
        return node

    return build(arr, 0)

def main():
    print('Hello World')

if __name__ == '__main__':
    main()