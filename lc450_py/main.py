

from typing import List, Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left

                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)

        return root


def preorder(root: Optional[TreeNode]) -> List[int]:

    res = []

    def _preorder(node: Optional[TreeNode]):
        if node:
            res.append(node.val)
            _preorder(node.left)
            _preorder(node.right)

    _preorder(root)
    return res



def test_tree_reference():
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)

    to_be_changed = root.right

    root.right = to_be_changed.right

    print(root.right.val)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()