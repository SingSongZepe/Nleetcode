

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        dq = deque([root])
        zigzag = False
        res = []

        while dq:
            lvl = []
            ndq = deque([])
            zigzag = not zigzag
            for _ in range(len(dq)):
                nd = dq.popleft()
                lvl.append(nd.val)
                if zigzag:
                    if nd.left:
                        ndq.appendleft(nd.left)
                    if nd.right:
                        ndq.appendleft(nd.right)
                else:
                    if nd.right:
                        ndq.appendleft(nd.right)
                    if nd.left:
                        ndq.appendleft(nd.left)

            dq = ndq
            res.append(lvl)

        return res






def main():
    print('Hello World')

if __name__ == '__main__':
    main()