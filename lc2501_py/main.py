

from typing import List
from math import sqrt

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        nums.sort()
        ml = 0
        d = {}

        for n in nums:
            n_sqrt = sqrt(n)
            if n_sqrt in d:
                d[n] = d[n_sqrt] + 1
            else:
                d[n] = 1

            if d[n] > ml:
                ml = d[n]
                if ml == 5:
                    return 5

        return ml if ml > 1 else -1

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        nums = sorted(set(nums), reverse=True)
        ml = 0
        st = set()

        for n in nums:
            l = 0
            curr = n

            st.add(curr)

            while curr in st:
                curr *= curr
                l += 1

            if l > ml:
                ml = l

        return ml if ml > 1 else -1





def main():
    print('Hello World')

if __name__ == '__main__':
    main()