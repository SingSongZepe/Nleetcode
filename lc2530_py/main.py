

from typing import List
from math import ceil, floor
import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        hp: List[int] = []

        for num in nums:
            heapq.heappush(hp, -num)

        p = 0
        for _ in range(k):
            v = heapq.heappop(hp)

            p += v
            heapq.heappush(hp, -ceil(-v / 3))

        return -p


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        hp: List[int] = [-num for num in nums]
        heapq.heapify(hp)

        p = 0
        for _ in range(k):
            # for negative number, floor equals to ceil function
            p -= heapq.heappushpop(hp, floor(hp[0] / 3))

        return p


def main():
    print('Hello World')

if __name__ == '__main__':
    main()