

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for k in range(len(nums)-1, -1, -1):
            left = 0
            right = k - 1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    count += right - left  # l, l+1,..., r-1, r
                    right -= 1
                else:
                    left += 1

        return count


#
class Solution1:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        fgtoe = [-1] * (2000 + 1)
        j = 0
        for i in range(len(fgtoe)):
            while j < len(nums) and nums[j] < i:
                j += 1
            fgtoe[i] = j

        ctr = 0
        rs = len(nums) * (len(nums) - 1) // 2 - 1
        rss = 0
        for ai in range(0, len(nums) - 2):
            nai = nums[ai]
            if nai != 0:
                ctr += sum(fgtoe[nai + nums[bi]] for bi in range(ai + 1, len(nums) - 1))
                rss += rs
            rs -= ai + 2
        return ctr - rss


def main():
    print('Hello World')

if __name__ == '__main__':
    main()