

from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        pf = [0]
        for n in nums:
            pf.append(pf[-1] + n)

        # do not need to delete a subarray
        if not pf[-1] % p:
            return 0

        map = {}
        min_len = float('inf')
        sm = pf[-1]
        for i, n in enumerate(pf):
            rm = (n - sm) % p
            if rm in map:
                min_len = min(min_len, i - map[rm])
            map[n % p] = i

        return min_len if min_len != len(nums) else -1


# better solution
class Solution1:
    def minSubarray(self, nums: List[int], p: int) -> int:

        sm = sum(nums)
        if not sm % p:
            return 0

        min_len = float('inf')
        mp = {0: -1}
        tot = 0
        for i, n in enumerate(nums):
            tot += n
            rm = (tot - sm) % p
            if rm in mp:
                min_len = min(min_len, i - mp[rm])
            mp[tot % p] = i

        return min_len if min_len != len(nums) else -1

def main():
    print('Hello World')

if __name__ == '__main__':
    main()