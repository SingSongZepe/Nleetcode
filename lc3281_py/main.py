

from typing import List

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:

        start.sort()

        left, right = 0, max(start) + d
        first = start[0]

        def check(mid) -> bool:
            x = first
            for s in start[1:]:
                x += mid
                if x > s + d:
                    return False
                x = max(x, s)

            return True

        while left < right:
            mid = (left + right + 1) // 2

            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left

class Solution1:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def fn(mid):
            x = -float('inf')
            for s in start:
                x += mid
                if x > s + d:
                    return False
                x = max(x, s)
            return True

        lo, hi = 0, max(start) + d
        while lo < hi:
            mid = lo + hi + 1 >> 1
            if fn(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo





        pass
def main():
    print('Hello World')

if __name__ == '__main__':
    main()