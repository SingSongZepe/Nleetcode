
from typing import List

# failed prefix sum method
# class Solution:
#     def maximumUniqueSubarray(self, nums: List[int]) -> int:
#         curr = 0
#         ps = [0] * len(nums)
#
#         for i in range(len(nums)):
#             curr += nums[i]
#             ps[i] = curr
#
#         l = -1
#         m = 0
#         d = {}
#         for r in range(len(nums)):
#             if nums[r] in d:
#                 idx = d[nums[r]]
#                 if idx > l:
#                     l = idx
#                     m = max(m, ps[r] - ps[l])
#             d[nums[r]] = r
#
#         m = max(m, ps[r] - (ps[l] if l != -1 else 0))
#         return m

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        l, m, curr = 0, 0, 0
        d = set()
        for numr in nums:
            while numr in d:
                d.remove(nums[l])
                curr -= nums[l]
                l += 1
            d.add(numr)
            curr += numr
            m = max(m, curr)

        return m

# maybe faster
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        l, m, curr = 0, 0, 0
        d = set()
        for numr in nums:
            if numr in d:
                while nums[l] != numr:
                    d.remove(nums[l])
                    curr -= nums[l]
                    l += 1
                l += 1
            else:
                d.add(numr)
                curr += numr
                if curr > m:
                    m = curr

        return m


def main():
    print('Hello World')

if __name__ == '__main__':
    main()