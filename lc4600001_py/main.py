
from typing import List

class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:

        nums.sort()

        res = 0
        n = len(nums)
        for i in range(n//3, n, 2):
            res += nums[i]

        return res


def main():
    print('Hello World')

if __name__ == '__main__':
    main()