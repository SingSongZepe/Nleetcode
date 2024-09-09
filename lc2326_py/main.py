

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)] # can't initialize by [[-1] * n] * m, because it will create m references to the same list

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, d = 0, 0, 0

        while head:
            res[x][y] = head.val
            head = head.next

            nx, ny = x + dirs[d][0], y + dirs[d][1]
            if 0 <= nx < m and 0 <= ny < n and res[nx][ny] == -1:
                x, y = nx, ny
            else:
                d = (d + 1) % 4
                x, y = x + dirs[d][0], y + dirs[d][1]

        return res


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        curr = head
        matrix = [[-1] * n for _ in range(m)]
        r = 0
        c = 0
        d_p = 0
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while curr:
            matrix[r][c] = curr.val
            curr = curr.next
            next_r, next_c = r + d[d_p % 4][0], c + d[d_p % 4][1]
            if 0 <= next_r < m and 0 <= next_c < n and matrix[next_r][next_c] == -1:
                r, c = next_r, next_c
            else:
                d_p += 1
                r, c = r + d[d_p % 4][0], c + d[d_p % 4][1]
        return matrix


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# a better solution, it does not use many 'if' to check turn around,
# but just count how long distance to move in each direction,
class Solution2:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        left, right, top, bottom = 0, n, 0, m
        temp = head
        matrix = [[0] * n for _ in range(m)]
        while left < right and top < bottom:

            for i in range(left, right):
                val = -1
                if temp:
                    val = temp.val
                    temp = temp.next
                matrix[top][i] = val
            top += 1

            for i in range(top, bottom):
                val = -1
                if temp:
                    val = temp.val
                    temp = temp.next
                matrix[i][right - 1] = val
            right -= 1

            if not (left < right and top < bottom): break

            for i in range(right - 1, left - 1, -1):
                val = -1
                if temp:
                    val = temp.val
                    temp = temp.next
                matrix[bottom - 1][i] = val
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                val = -1
                if temp:
                    val = temp.val
                    temp = temp.next
                matrix[i][left] = val
            left += 1
        return matrix


def build_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head


def main():
    print('Hello World')

if __name__ == '__main__':
    main()