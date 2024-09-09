


from typing import List

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:

        # A B C
        # from A to C, you get 2*A points
        # from A to B and B to C, you get A+B points
        # if B smaller than A, then just jump from A to C and get 2*A points

        cp, f, scr = 0, nums[0], 0

        for i in range(1, len(nums)):
            if nums[i] > f:
                scr += (i - cp) * f
                cp = i
                f = nums[i]

        return scr + (len(nums) - cp - 1) * f


def main():
    print('Hello World')

if __name__ == '__main__':
    main()