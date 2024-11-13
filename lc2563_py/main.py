

from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        n = len(nums)
        if n == 1:
            return 0

        nums.sort()
        l = 0

        for r in range(1, n):
            pass

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.countPairs(nums, upper) - self.countPairs(nums, lower - 1)

    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += right - left
                left += 1

        return count

def main():
    print('Hello World')

if __name__ == '__main__':
    main()