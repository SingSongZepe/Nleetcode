
from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:

        res = [0] * len(nums)
        res[0] = 2 * nums[0]
        m = nums[0]
        for i in range(1, len(nums)):
            m = max(m, nums[i])
            res[i] = res[i-1] + m + nums[i]

        return res

class Solution1:
    def findPrefixScore(self, nums: List[int]) -> List[int]:

        m = nums[0]
        nums[0] *= 2

        for i in range(1, len(nums)):
            m = max(m, nums[i])
            nums[i] = nums[i-1] + m + nums[i]
            # nums[i] += nums[i-1] + m

        return nums



def main():
    print('Hello World')

if __name__ == '__main__':
    main()