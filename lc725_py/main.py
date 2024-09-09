


from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        def get_length(head: Optional[ListNode]) -> int:
            n = 0
            while head:
                n += 1
                head = head.next
            return n

        n = get_length(head)
        part_len, remain = n // k, n % k
        res = []

        while head and k > 0:
            ph = head
            if remain > 0:
                for i in range(part_len):
                    head = head.next
                remain -= 1
            else:
                for i in range(part_len - 1):
                    head = head.next
            k -= 1
            head.next, head = None, head.next
            res.append(ph)

        while k > 0:
            res.append(None)
            k -= 1

        return res

def build_list(nums: List[int]) -> Optional[ListNode]:
    if not nums:
        return None
    head = ListNode(nums[0])
    curr = head
    for num in nums[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head

def print_list(head: Optional[ListNode]) -> None:
    while head:
        print(head.val, end='->')
        head = head.next
    print('None')

def main():
    print('Hello World')

if __name__ == '__main__':
    main()