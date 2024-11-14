

from typing import List
from math import ceil

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        l, r = ceil(sum(quantities) / n), max(quantities)

        def need(single: int) -> int:
            return sum(ceil(q / single) for q in quantities)

        mi = float('inf')
        while l <= r:
            mid = (l + r + 1) // 2
            ned = need(mid)

            if ned == n:
                reduce = float('inf')
                for q in quantities:
                    ned_q = ceil(q / mid)
                    reduce = min(reduce, (mid * ned_q - q) // ned_q)
                return mid - reduce
            elif ned < n:
                mi = min(mi, mid)
                r = mid - 1
            else:
                l = mid + 1

        return mi



import math
class Solution:
    def _solve_with_bin_search_by_value(self, n: int, q: List[int]) -> int:
        # TC: O(m*log(m) + m*log(p)), where p := max(q)
        q.sort(reverse=True)
        m = len(q)
        left, right = 1, q[0]
        res = right
        while left <= right:
            free_slots = n - m
            mid = (left + right) // 2
            i = 0
            while i < m and free_slots >= 0:
                slots = math.ceil(q[i] / mid) - 1
                if not slots:
                    break
                free_slots -= slots
                i += 1
            if free_slots < 0:  # not enough slots
                left = mid + 1
            else:
                right = mid - 1
                res = mid

        return res

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if n == len(quantities):
            return max(quantities)

        return self._solve_with_bin_search_by_value(n, quantities)

def main():
    print('Hello World')

if __name__ == '__main__':
    main()