

from typing import List
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        l = len(nums)
        prev = nums[0]
        count = 0
        for p in range(1, l-1):
            if nums[p] == nums[p+1]:
                continue
            last = p + 1

            if (prev > nums[p] and nums[last] > nums[p]) or (prev < nums[p] and nums[last] < nums[p]):
                count += 1

            prev = nums[p]

        return count


class Solution1:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        if nums[0] > nums[1]:
            state = 0
        elif nums[1] > nums[0]:
            state = 1
        else:
            state = -1

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            elif nums[i] > nums[i - 1]:
                if state == 0:
                    ans += 1
                    state = 1
                else:
                    state = 1
            elif nums[i] < nums[i - 1]:
                if state == 1:
                    ans += 1
                    state = 0
                else:
                    state = 0
        return ans

# new daily
class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        i, left, n = 1, nums[0], len(nums)
        res = 0
        while i < n - 1:
            if (left < nums[i] and nums[i] > nums[i+1]) or (left > nums[i] and nums[i] < nums[i+1]):
                left = nums[i]
                res += 1
            i += 1
            while i < n - 1 and nums[i] == nums[i+1]:
                i += 1

        return res



def main():
    print('Hello World')

if __name__ == '__main__':
    main()