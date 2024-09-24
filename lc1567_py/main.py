

from typing import List


# DP solution
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        n = len(nums)
        p, n = [0] * n, [0] * n
        p[0] = 1 if nums[0] > 0 else 0
        n[0] = 1 if nums[0] < 0 else 0
        res = p[0]

        for i, v in enumerate(nums[1:], start=1):
            if v > 0:
                p[i] = 1 + p[i-1]
                n[i] = 1 + n[i-1] if n[i-1] > 0 else 0
            elif v < 0:
                p[i] = 1 + n[i-1] if n[i-1] > 0 else 0
                n[i] = 1 + p[i-1]
            res = max(res, p[i])

        return res

class Solution1:
    def getMaxLen(self, nums: List[int]) -> int:
        nums.append(0)
        sign, l, r = 1, 0, 0
        first_neg, last_neg = None, None
        mx = 0

        while r < len(nums):
            if nums[r] == 0:
                if r > 0:
                    if sign == 1:
                        mx = max(mx, r - l)
                    else:
                        mx = max(mx, last_neg - l, r - first_neg - 1)
                    sign = 1
                    first_neg, last_neg = None, None
                l = r + 1

            elif nums[r] < 0:
                if first_neg is None:
                    first_neg = r
                last_neg = r
                sign = -sign

            r += 1
        return mx

class Solution1b:
    def getMaxLen(self, nums: List[int]) -> int:
        sign, l, r = 1, 0, 0
        first_neg, last_neg = None, None
        mx = 0

        while r < len(nums):
            if nums[r] == 0:
                if r > 0:
                    if sign == 1:
                        mx = max(mx, r - l)
                    else:
                        mx = max(mx, last_neg - l, r - first_neg - 1)
                    sign = 1
                    first_neg, last_neg = None, None
                l = r + 1

            elif nums[r] < 0:
                if first_neg is None:
                    first_neg = r
                last_neg = r
                sign = -sign

            r += 1
        return max(mx, r - l) if sign == 1 else max(mx, last_neg - l, r - first_neg - 1)


class Solution2:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = [0] * n, [0] * n
        if nums[0] > 0: pos[0] = 1
        if nums[0] < 0: neg[0] = 1
        ans = pos[0]
        for i in range(1, n):
            if nums[i] > 0:
                pos[i] = 1 + pos[i - 1]
                neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
                neg[i] = 1 + pos[i - 1]
            ans = max(ans, pos[i])
        return ans

# two pointers solution
class Solution3:
    def getMaxLen(self, nums: List[int]) -> int:
        nums.append(0)
        ans = left = negs = 0
        first_neg, last_neg = None, None
        for right in range(len(nums)):
            if nums[right] == 0:
                if right > 0:
                    if negs % 2 == 0:
                        ans = max(ans, right - left)
                    else:
                        ans = max(ans, right - first_neg - 1, last_neg - left)
                    negs = 0
                    first_neg, last_neg = None, None
                left = right + 1

            elif nums[right] < 0:
                negs += 1
                if first_neg is None:
                    first_neg = right
                last_neg = right

        return ans

def main():
    print('Hello World')

if __name__ == '__main__':
    main()