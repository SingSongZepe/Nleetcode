

from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        stack: List[int] = []
        res = 0
        for idx, n in enumerate(nums):
            if not stack or n < nums[stack[-1]]:
                stack.append(idx)
            else:
                p = len(stack) - 1
                while p >= 0 and n >= nums[stack[p]]:
                    diff = idx - stack[p]
                    if diff > res:
                        res = diff
                    p -= 1

        return res

class Solution1:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []

        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)

        max_width = 0

        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                width = j - stack.pop()
                max_width = max(max_width, width)

        return max_width









def main():
    print('Hello World')

if __name__ == '__main__':
    main()