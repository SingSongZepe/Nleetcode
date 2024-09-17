


from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# value label approach
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr = head
        while curr:
            if curr.val == None:
                return True
            curr.val = None
            curr = curr.next

        return False


# fast and slow pointer approach
class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False



def build_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

def print_list(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(curr.val, end='->' if curr.next else '')
        curr = curr.next

def main():
    print('Hello World')

if __name__ == '__main__':
    main()