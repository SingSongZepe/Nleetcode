

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st = set(nums)
        longest = 0

        for n in nums:
            # eventually n-1 will be longer than n
            # so, we have no need to iterate by n
            if n-1 in st:
                continue

            length = 0
            while n in st:
                n += 1
                length += 1

            if length > longest:
                longest = length

        return longest


# sort solution
class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()

        counts = []
        count = 1
        y = nums[0]
        for x in nums[1:]:
            if x != y + 1:
                counts.append(count)
                count = 0
            y = x
            count += 1
        counts.append(count)

        return max(counts)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()