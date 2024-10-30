
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


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        dq = deque([root])

        while dq:
            lvl_tot = len(dq)
            for i in range(lvl_tot):
                node = dq.popleft()
                if i < lvl_tot:
                    node.next = dq[0]
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return root


class Solution1:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftmost = root
        while leftmost.left:
            t = leftmost
            while t:
                t.left.next = t.right
                if t.next:
                    t.right.next = t.next.left
                t = t.next
            leftmost = leftmost.left
        return root



# since this is a perfect binary tree
class Solution1:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        lm = root
        while lm.left:
            tmp = lm
            while tmp:
                tmp.left.next = tmp.right
                if tmp.next:
                    tmp.right.next = tmp.next.left
                tmp = tmp.next
            lm = lm.left

        return root







def main():
    print('Hello World')

if __name__ == '__main__':
    main()