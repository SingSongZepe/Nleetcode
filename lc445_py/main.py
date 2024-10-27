

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1 = []
        stk2 = []
        carry = False

        c1, c2 = l1, l2
        while c1:
            stk1.append(c1)
            c1 = c1.next
        while c2:
            stk2.append(c2)
            c2 = c2.next

        if len(stk1) < len(stk2):
            l1, l2 = l2, l1
            stk1, stk2 = stk2, stk1

        while stk1 and stk2:
            c1, c2 = stk1.pop(), stk2.pop()
            sum = c1.val + c2.val + carry
            c1.val = sum % 10
            if sum > 9:
                carry = True
            else:
                carry = False

        while carry and stk1:
            c1 = stk1.pop()
            if c1.val == 9:
                c1.val = 0
            else:
                c1.val += 1
                carry = False

        if carry:
            new = ListNode(1)
            new.next = l1
            return new
        else:
            return l1


# same method, but better written
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        node = None
        temp = 0
        while stack1 or stack2 or temp:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            temp, val = divmod(v1 + v2 + temp, 10)
            res = ListNode(val, node)
            node = res

        return res

def build_list(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    curr = dummy

    for n in arr:
        curr.next = ListNode(n)
        curr = curr.next

    return dummy.next

def print_list(root: Optional[ListNode]) -> None:

    while root:
        print(f'{root.val}->', end='')
        root = root.next

    print('done')



def main():
    print('Hello World')

if __name__ == '__main__':
    main()