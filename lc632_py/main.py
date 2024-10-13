
from typing import List
import heapq

class TupleForHeap:
    def __init__(self, value, row_idx, col_idx):
        self.value = value
        self.i = row_idx
        self.j = col_idx

    def __neg__(self):
        return TupleForHeap(-self.value, self.i, self.j)

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash((self.value, self.i, self.j))

class DualHeap:
    def __init__(self):
        self.hp_min = []  # 最小堆
        self.hp_max = []  # 最大堆（存储负值以模拟最大堆）
        self.count = {}  # 用于追踪有效元素的计数

    def push(self, tp: TupleForHeap):
        heapq.heappush(self.hp_min, tp)  # 添加到最小堆
        heapq.heappush(self.hp_max, -tp)  # 添加到最大堆（取负）
        self.count[tp] = self.count.get(tp, 0) + 1

    def pop_min(self):
        while self.hp_min:
            min_value = heapq.heappop(self.hp_min)
            if self.count[min_value] > 0:  # 验证有效元素
                self.count[min_value] -= 1
                return min_value

    def pop_max(self):
        while self.hp_max:
            max_value = -heapq.heappop(self.hp_max)
            if self.count[max_value] > 0:  # 验证有效元素
                self.count[max_value] -= 1
                return max_value

    def get_min(self) -> TupleForHeap:
        while self.hp_min:
            min_value = self.hp_min[0]  # 查看最小堆的根元素
            if self.count[min_value] > 0:  # 验证有效元素
                return min_value
            else:
                heapq.heappop(self.hp_min)  # 弹出无效元素

    def get_max(self) -> TupleForHeap:
        while self.hp_max:
            max_value = -self.hp_max[0]  # 查看最大堆的根元素
            if self.count[max_value] > 0:  # 验证有效元素
                return max_value
            else:
                heapq.heappop(self.hp_max)  # 弹出无效元素


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        # create a min heap of tuples (row_idx, column_idx) for each row in nums
        dp = DualHeap()

        for i in range(len(nums)):
            dp.push(TupleForHeap(nums[i][0], i, 0))

        rs = dp.get_min().value
        re = dp.get_max().value

        while True:
            # pop the smallest num and index from the heap
            tp = dp.pop_min()
            if tp.j < len(nums[tp.i]) - 1:
                dp.push(TupleForHeap(nums[tp.i][tp.j+1], tp.i, tp.j+1))
                # heapq.heappush(hp_min, (nums[i][ j +1], i, j+ 1))
            else:
                return [rs, re]

            # get the new smallest and largest range
            nrs = dp.get_min().value
            nre = dp.get_max().value

            if nre - nrs < re - rs:
                rs, re = nrs, nre

        return [rs, re]


from typing import List, Dict
from collections import defaultdict

# sliding and two pointers solution
class Solution1:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        d: Dict[int, List[int]] = defaultdict(list)
        for i, evs in enumerate(nums):
            for v in evs:
                d[v].append(i)

        keys = sorted(d.keys())
        lo = 0
        n = len(nums)
        dd = defaultdict(int)
        le, ri = -1, float('Inf')
        have = 0

        for hi in range(len(keys)):
            for x in d[keys[hi]]:
                dd[x] += 1
                if dd[x] == 1:
                    have += 1

            while have == n:
                curr = keys[hi] - keys[lo]
                if ri - le > curr:
                    ri = keys[hi]
                    le = keys[lo]
                for x in d[keys[lo]]:
                    dd[x] -= 1
                    if dd[x] == 0:
                        have -= 1
                lo += 1

        return [le, ri]


import heapq
from typing import List


class TupleForHeap1:
    def __init__(self, value, row_idx, col_idx):
        self.value = value
        self.row_idx = row_idx
        self.col_idx = col_idx

    def __lt__(self, other):
        return self.value < other.value


# better solution in DualHeap solution
class Solution2:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')

        for i in range(len(nums)):
            heapq.heappush(min_heap, TupleForHeap1(nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])

        range_start, range_end = -1e5, 1e5

        while True:
            current_min = min_heap[0].value
            if current_max - current_min < range_end - range_start:
                range_start, range_end = current_min, current_max

            top = heapq.heappop(min_heap)

            if top.col_idx + 1 == len(nums[top.row_idx]):
                break

            next_value = nums[top.row_idx][top.col_idx + 1]
            heapq.heappush(min_heap, TupleForHeap1(next_value, top.row_idx, top.col_idx + 1))
            current_max = max(current_max, next_value)

        return [range_start, range_end]

def main():
    print('Hello World')


if __name__ == '__main__':
    main()
