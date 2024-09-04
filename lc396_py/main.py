

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        F, n = sum(num * i for i, num in enumerate(nums)), len(nums)

        Fm = F
        sm = sum(nums)
        for k in range(1, len(nums)):
            F = F + sm - n * nums[n-k]
            if Fm < F:
                Fm = F

        return Fm

def main():
    print('Hello World')

if __name__ == '__main__':
    main()