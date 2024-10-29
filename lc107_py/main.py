

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        stk = deque([root])
        res = []

        while stk:
            lvl = []

            for _ in range(len(stk)):
                nd = stk.popleft()
                lvl.append(nd.val)
                if nd.left:
                    stk.append(nd.left)
                if nd.right:
                    stk.append(nd.right)

            res.append(lvl)

        return res[::-1]



def main():
    print('Hello World')

if __name__ == '__main__':
    main()