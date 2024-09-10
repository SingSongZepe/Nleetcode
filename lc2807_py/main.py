


from typing import Optional, List
from math import gcd

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # def gcd(a, b):
        #     if b == 0:
        #         return a
        #     return gcd(b, a % b)

        curr = head
        while curr.next:
            node = ListNode(gcd(curr.val, curr.next.val), curr.next)
            curr.next = node
            curr = curr.next.next

        return head



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
    while head:
        print(head.val, end='->')
        head = head.next
    else:
        print('None')

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()