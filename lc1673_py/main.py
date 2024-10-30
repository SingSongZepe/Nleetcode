

from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) + len(nums) - i > k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stk = []
        max_drop = n - k
        for i in range(n):
            while max_drop and stk and stk[-1] > nums[i]:
                stk.pop()
                max_drop -= 1
            stk.append(nums[i])
        return stk[:k]


def main():
    print('Hello World')

if __name__ == '__main__':
    main()