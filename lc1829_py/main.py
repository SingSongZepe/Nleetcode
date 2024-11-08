

from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        x, n, m = 0, len(nums), (1 << maximumBit) - 1
        for i in range(n):
            x ^= nums[i]
            nums[i] = m - x

        nums.reverse()
        return nums













        pass


def main():
    print('Hello World')

if __name__ == '__main__':
    main()