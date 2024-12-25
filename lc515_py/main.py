
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        dp = deque([root])
        lvl_ms: List[int] = []

        while dp:

            lvl_m = float('-inf')
            for _ in range(len(dp)):
                nd = dp.popleft()
                if nd.left:
                    dp.append(nd.left)
                if nd.right:
                    dp.append(nd.right)

                lvl_m = max(lvl_m, nd.val)

            lvl_ms.append(lvl_m)

        return lvl_ms

def main():
    print('Hello World')

if __name__ == '__main__':
    main()