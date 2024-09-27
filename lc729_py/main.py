


# class MyCalendar:
#
#     def __init__(self):
#         self.starts = []
#         self.ends = []
#
#
#     def book(self, start: int, end: int) -> bool:
#         if not self.starts:
#             self.starts.append(start)
#             self.ends.append(end)
#             return True
#         else:
#             # binary search to find start index
#             left, right = 0, len(self.starts) - 1
#             result_index = -1
#
#             while left <= right:
#                 mid = (left + right) // 2
#                 if self.starts[mid] < start:
#                     result_index = mid
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#
#             if start < self.ends[result_index]:
#                 return False
#
#             self.starts.insert(result_index + 1, start)
#             self.ends.insert(result_index + 1, end)
#             return True


class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        for s, e in zip(self.starts, self.ends):
            if not (end <= s or start >= e):
                return False

        self.starts.append(start)
        self.ends.append(end)
        return True


class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, start, end) -> bool:
        if start >= self.end:
            if not self.right:
                self.right = TreeNode(start, end)
                return True
            return self.right.insert(start, end)
        elif end <= self.start:
            if not self.left:
                self.left = TreeNode(start, end)
                return True
            return self.left.insert(start, end)

        # overlapping
        return False


class MyCalendar1:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = TreeNode(start, end)
            return True
        return self.root.insert(start, end)


class Node:
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.l = self.r = None

    def insert(self, start, end):
        if self.s >= end:
            if not self.l:
                self.l = Node(start, end)
                return True
            return self.l.insert(start, end)
        elif self.e <= start:
            if not self.r:
                self.r = Node(start, end)
                return True
            return self.r.insert(start, end)

        # overlapping
        return False

# segment tree solution
class MyCalendar2:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(start, end)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()