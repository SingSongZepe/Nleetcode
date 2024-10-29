

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, pre: List[int], ino: List[int]) -> Optional[TreeNode]:

        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])

        root_v = pre[0]
        p = 0
        while ino[p] != root_v:
            p += 1

        root = TreeNode(root_v)
        root.left = self.buildTree(pre[1:1+p], ino[:p])
        root.right = self.buildTree(pre[p+1:], ino[p+1:])
        return root


class Solution1:
    def buildTree(self, pre: List[int], ino: List[int]) -> Optional[TreeNode]:

        d = {ino[i]: i for i in range(len(ino))}

        # preorder front, preorder rear
        def build(pref: int, prer: int, inof: int, inor: int) -> Optional[TreeNode]:
            if pref >= prer:
                return None

            root = TreeNode(pre[pref])
            p = d[pre[pref]]

            root.left = build(pref+1, pref+1+p-inof, inof, p)
            root.right = build(pref+p+1-inof, prer, p+1, inor)
            return root

        return build(0, len(pre), 0, len(pre))


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



def main():
    print('Hello World')

if __name__ == '__main__':
    main()