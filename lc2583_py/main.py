
from typing import Optional

from collections import deque
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        dq = deque([root])
        hp = []

        while dq:
            sm = 0
            for i in range(len(dq)):
                node = dq.popleft()
                sm -= node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            heapq.heappush(hp, sm)


        i = 1
        while i < k and hp:
            heapq.heappop(hp)

        if hp:
            return -heapq.heappop(hp)
        else:
            return -1





def main():
    print('Hello World')

if __name__ == '__main__':
    main()