

from typing import List, Optional
from collections import deque

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# bfs
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None

        dq = deque([root])

        while dq:
            lvl_tot = len(dq)
            for i in range(lvl_tot):
                node = dq.popleft()
                if i < lvl_tot-1:
                    node.next = dq[0]
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        lm = root
        dummy = Node()

        while lm:
            tmp = lm
            dumm = dummy
            while tmp:
                if tmp.left:
                    dumm.next = tmp.left
                    dumm = dumm.next
                if tmp.right:
                    dumm.next = tmp.right
                    dumm = dumm.next
                tmp = tmp.next

            lm = dummy.next
            dummy.next = None

        return root



def main():
    print('Hello World')

if __name__ == '__main__':
    main()