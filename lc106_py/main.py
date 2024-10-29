

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        d = {inorder[i]: i for i in range(len(inorder))}

        def build(inof: int, inor: int, postf: int, postr: int) -> Optional[TreeNode]:
            if postf >= postr:
                return None

            root = TreeNode(postorder[postr-1])
            p = d[postorder[postr-1]]

            root.left = build(inof, p, postf, postf+p-inof)
            root.right = build(p+1, postr, postf+p-inof, postr-1)
            return root

        return build(0, len(inorder), 0, len(inorder))





def preorder(root: Optional[TreeNode]) -> List[int]:
    res = []

    def _preorder(nd: Optional[TreeNode]) -> None:
        if not nd:
            return
        res.append(nd.val)
        _preorder(nd.left)
        _preorder(nd.right)

    _preorder(root)
    return res

def inoreder(root: Optional[TreeNode]) -> List[int]:
    res = []

    def _inorder(nd: Optional[TreeNode]) -> None:
        if not nd:
            return
        _inorder(nd.left)
        res.append(nd.val)
        _inorder(nd.right)

    _inorder(root)
    return res

def postoreder(root: Optional[TreeNode]) -> List[int]:
    res = []

    def _postoreder(nd: Optional[TreeNode]) -> None:
        if not nd:
            return
        _postoreder(nd.left)
        _postoreder(nd.right)
        res.append(nd.val)

    _postoreder(root)
    return res

def main():
    print('Hello World')

if __name__ == '__main__':
    main()