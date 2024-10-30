

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# top-down solution
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        head = TreeNode(-1)

        def _flatten(node: Optional[TreeNode]):
            if not node:
                return

            nonlocal head
            head.right = node
            head = head.right

            right = node.right
            node.left = None
            node.right = None

            _flatten(node.left)
            _flatten(right)


        _flatten(root)



# bottom-up
class Solution1:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def _flatten(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None

            left_tail = _flatten(node.left)
            right_tail = _flatten(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            return right_tail or left_tail or node

        _flatten(root)







def print_list(root: Optional[TreeNode]):

    while root:
        print(root.val, end='->')
        root = root.right


def main():
    print('Hello World')

if __name__ == '__main__':
    main()