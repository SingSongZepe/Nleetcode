

from typing import List




# Time Out
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        lsts: List[int] = []
        intervals.sort()

        for s, e in intervals:
            insert = False
            for i, lst in enumerate(lsts):
                if s > lst:
                    lsts[i] = e
                    insert = True
                    break

            if not insert:
                lsts.append(e)

        return len(lsts)


import heapq

class Solution1:
    def minGroups(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        heap = []
        intervals.sort(key=lambda x: x[0])

        for s, e in intervals:
            if heap and s > heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, e)

        return len(heap)


# two pointers solution
class Solution2:
    def minGroups(self, intervals: List[List[int]]) -> int:
        starts = sorted(s for s, e in intervals)
        ends = sorted(e for s, e in intervals)

        max_groups = 0
        current_groups = 0
        start_ptr = 0
        end_ptr = 0

        while start_ptr < len(starts):
            if starts[start_ptr] <= ends[end_ptr]:
                # A new interval starts, increment the current group count
                current_groups += 1
                max_groups = max(max_groups, current_groups)
                start_ptr += 1
            else:
                # An interval ends, decrement the current group count
                current_groups -= 1
                end_ptr += 1

        return max_groups

def main():
    print('Hello World')

if __name__ == '__main__':
    main()