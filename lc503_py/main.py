

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)

        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n
            stack.append(i)

        # circle processing
        for num in nums:
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num

        return res



def main():
    print('Hello World')

if __name__ == '__main__':
    main()