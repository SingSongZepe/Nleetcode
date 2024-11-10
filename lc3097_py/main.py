

from typing import List
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        l, r, n = 0, 0, len(nums)
        m = n
        curr = 0
        while r < n:
            curr |= nums[r]
            if curr >= k:
                ll = r
                ncurr = 0
                while ll >= l:
                    ncurr |= nums[ll]
                    if ncurr >= k:
                        break
                    ll -= 1
                m = min(r - ll + 1, m)
                # if ll != l:
                #     curr = 0
                #     for i in range(ll, r):
                #         curr |= nums[i]
                l = ll
            r += 1

        return m if m != n else -1


# maybe a better solution
from math import inf
class Solution1:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf
        d = dict()
        for i, x in enumerate(nums):
            d = {or_ | x: left for or_, left in d.items()}
            d[x] = i

            for or_, left in d.items():
                if or_ >= k:
                    ans = min(ans, i - left + 1)

        return ans if ans < inf else -1



class Solution2:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        n = len(nums)
        m = n + 1
        d = {}
        for i in range(n):
            d = {ors | nums[i]: lp for ors, lp in d.items()}
            d[nums[i]] = i

            for ors, lp in d.items():
                if ors >= k:
                    m = min(m, i - lp + 1)

        return m if m != n+1 else -1




def main():
    print('Hello World')

if __name__ == '__main__':
    main()