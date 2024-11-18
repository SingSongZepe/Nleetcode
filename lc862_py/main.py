

from typing import List
from itertools import accumulate
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] + list(accumulate(nums))
        shortest = len(nums) + 1
        increase_sum_index = deque()

        for right in range(len(prefix_sum)):
            right_sum = prefix_sum[right]

            while increase_sum_index and right_sum <= prefix_sum[increase_sum_index[-1]]:
                increase_sum_index.pop()

            while increase_sum_index:
                left = increase_sum_index[0]
                if right_sum - prefix_sum[left] < k:
                    break
                shortest = min(shortest, right - left)
                increase_sum_index.popleft()

            increase_sum_index.append(right)

        if shortest < len(nums) + 1:
            return shortest

        return -1
















        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()