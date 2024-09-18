

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = [str(num) for num in nums]
        nums.sort(key=lambda x: x*2, reverse=True)

        if nums[0] == '0':
            return '0'

        return ''.join(nums)


def main():
    print('Hello World')

if __name__ == '__main__':
    main()