

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# easy solution using DFS and backtracking
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def check_path(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
            if not head:
                return True
            if not root or head.val != root.val:
                return False
            return check_path(head.next, root.left) or check_path(head.next, root.right)

        if not root:
            return False

        if check_path(head, root):
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

class Solution1:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # Build the pattern and prefix table from the linked list
        pattern = [head.val]
        prefix_table = [0]
        pattern_index = 0
        head = head.next

        while head:
            while pattern_index > 0 and head.val != pattern[pattern_index]:
                pattern_index = prefix_table[pattern_index - 1]
            pattern_index += 1 if head.val == pattern[pattern_index] else 0
            pattern.append(head.val)
            prefix_table.append(pattern_index)
            head = head.next

        # Perform DFS to search for the pattern in the tree
        return self._search_in_tree(root, 0, pattern, prefix_table)

    def _search_in_tree(self, node: Optional[TreeNode], pattern_index: int, pattern: List[int], prefix_table: List[int]) -> bool:
        if not node:
            return False

        while pattern_index > 0 and node.val != pattern[pattern_index]:
            pattern_index = prefix_table[pattern_index - 1]
        pattern_index += 1 if node.val == pattern[pattern_index] else 0

        # Check if the pattern is fully matched
        if pattern_index == len(pattern):
            return True

        # Recursively search left and right subtrees
        return self._search_in_tree(node.left, pattern_index, pattern, prefix_table) or \
               self._search_in_tree(node.right, pattern_index, pattern, prefix_table)





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

def build_tree(nums: List[int]) -> Optional[TreeNode]:

    def build(nums: List[int], idx: int) -> Optional[TreeNode]:
        if idx >= len(nums) or nums[idx] is None:
            return None
        node = TreeNode(nums[idx])
        node.left = build(nums, 2*idx+1)
        node.right = build(nums, 2*idx+2)
        return node

    return build(nums, 0)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()