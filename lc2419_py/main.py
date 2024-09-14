

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m, cnt, mcnt = max(nums), 0, 0

        for n in nums:
            if n == m:
                cnt += 1
            else:
                mcnt = max(mcnt, cnt)
                cnt = 0

        return max(mcnt, cnt)


# class Solution1:
#     def longestSubarray(self, nums: List[int]) -> int:
#         cnt, mcnt = 0, 0
#         for n in nums:
#


def main():
    print('Hello World')

if __name__ == '__main__':
    main()