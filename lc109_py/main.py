

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def build(i: int, e: int) -> Optional[TreeNode]:
            if i >= e:
                return None

            mid = (i+e) // 2
            root = TreeNode(arr[mid])
            root.left = build(i, mid)
            root.right = build(mid+1, e)
            return root

        return build(0, len(arr))

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)

        pre = None
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        if pre:
            pre.next = None
        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root


def build_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    head.next = build_linked_list(arr[1:])
    return head

def print_linked_list(head: Optional[ListNode]):
    while head:
        print(head.val, end='->')
        head = head.next

def collect_linked_list(head: Optional[ListNode]) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next

    return res

def inorder(root: Optional[TreeNode]) -> List[int]:

    res = []

    def _inorder(nd: Optional[TreeNode]):
        if nd:
            _inorder(nd.left)
            res.append(nd.val)
            _inorder(nd.right)

    _inorder(root)
    return res

def main():
    print('Hello World')

if __name__ == '__main__':
    main()