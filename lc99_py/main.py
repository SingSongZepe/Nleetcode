

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# morris traversal
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        curr, prev = root, None
        first, second = None, None
        while curr:
            if not curr.left:
                if prev and curr.val < prev.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right is not curr:
                    temp = temp.right
                if temp.right is None:
                    temp.right = curr
                    curr = curr.left
                else:
                    temp.right = None
                    if prev and curr.val < prev.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right

        first.val, second.val = second.val, first.val



class Solution1:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr, prev, a, b = root, None, None, None
        while curr:
            if not curr.left:
                if prev and curr.val < prev.val:
                    if not a:
                        a = prev
                    b = curr
                prev = curr
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right is not curr:
                    temp = temp.right
                if temp.right is curr:
                    temp.right = None
                    if prev and curr.val < prev.val:
                        if not a:
                            a = prev
                        b = curr
                    prev = curr
                    curr = curr.right
                else:
                    temp.right = curr
                    curr = curr.left

        a.val,b.val = b.val, a.val



def build_tree(arr: List[int]) -> Optional[TreeNode]:
    def build(arr, idx) -> Optional[TreeNode]:
        if idx >= len(arr) or arr[idx] is None:
            return None
        node = TreeNode(arr[idx])
        node.left = build(arr, 2*idx+1)
        node.right = build(arr, 2*idx+2)
        return node
    return build(arr, 0)

def inorder_traversal(node: Optional[TreeNode]) -> List[int]:
    if not node:
        return []
    return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)


def inorder_traversal1(node: Optional[TreeNode]) -> List[int]:
    res = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)

    inorder(node)
    return res

def morris_inorder_traversal(node: Optional[TreeNode]) -> List[int]:
    res = []
    curr = node
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            temp = curr.left
            while temp.right and temp.right is not curr:
                temp = temp.right
            if temp.right is None:
                temp.right = curr
                curr = curr.left
            else:
                temp.right = None
                res.append(curr.val)
                curr = curr.right
    return res


def main():
    print('Hello World')

if __name__ == '__main__':
    main()